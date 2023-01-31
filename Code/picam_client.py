# picam_client.py
"""
Brief: Teleoperates a robot around and streams the video from the client on the Raspberry Pi 
       to a server running on a Laptop for further processing. 
Course: ENPM673 - Perception for Autonomous Robotics [Project-04]
        University of Maryland, College Park (MD)
Date: 9th May, 2022
"""

import io
import socket
import struct
import time
import picamera
import RPi.GPIO as gpio
from pynput import keyboard

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

# Setting up the motor pins on the Motor Driver 
gpio.setup(31, gpio.OUT) # IN1
gpio.setup(33, gpio.OUT) # IN2
gpio.setup(35, gpio.OUT) # IN3
gpio.setup(37, gpio.OUT) # IN4

stop_flag = 0    # Flag to stop streaming video to server


def teleopRobot(key):
    global stop_flag
    
    if key.char == 'w':
        moveForward(0.5)
    elif key.char == 'z':
        moveReverse(0.5)
    elif key.char == 's':
        rotateRight(0.5)
    elif key.char == 'a':
        rotateLeft(0.5)
    elif key.char == 'p':
        listener.stop()
        stop_flag = 1
        gpio.cleanup()
    

def stopRobot():
    # Set all pins low
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)


def moveForward(tf):
    # For Left wheels
    gpio.output(31, True)
    gpio.output(33, False)
    
    # For Right wheels
    gpio.output(35, False)
    gpio.output(37, True)
    
    # Move forward for 'tf' seconds
    time.sleep(tf)
    
    # Send all pins low
    stopRobot()


def moveReverse(tf):
    # For Left wheels
    gpio.output(31, False)
    gpio.output(33, True)
    
    # For Right wheels
    gpio.output(35, True)
    gpio.output(37, False)
    
    # Move backward for 'tf' seconds
    time.sleep(tf)
    
    # Send all pins low
    stopRobot()


def rotateLeft(tf):
    # For Left wheels
    gpio.output(31, False)
    gpio.output(33, True)
    
    # For Right wheels
    gpio.output(35, False)
    gpio.output(37, True)
    
    # Rotate left for 'tf/4' seconds
    time.sleep(tf/4.0)
    
    # Send all pins low
    stopRobot()


def rotateRight(tf):
    # For Left wheels
    gpio.output(31, True)
    gpio.output(33, False)
    
    # For Right wheels
    gpio.output(35, True)
    gpio.output(37, False)
    
    # Rotate right for 'tf/4' seconds
    time.sleep(tf/4.0)
    
    # Send all pins low
    stopRobot()

# Initialize the client socket connection
client_socket = socket.socket()
client_socket.connect(('<insert-server-ip-address>', 8000))
connection = client_socket.makefile('wb')

listener = keyboard.Listener(on_press=teleopRobot)
listener.start()

try:

    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        time.sleep(2)

        # Note: The camera feed is rotated by 180 deg on the server side.

        start = time.time()
        count = 0    # Keeps track of number frames sent
        stream = io.BytesIO()
        
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):

            if stop_flag == 1:
                break
            
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()

            stream.seek(0)
            connection.write(stream.read())
            count += 1
            
            stream.seek(0)
            stream.truncate()
    
    connection.write(struct.pack('<L', 0))

finally:

    connection.close()
    client_socket.close()
    finish = time.time()

print('Frame Rate', (count / (finish-start)))