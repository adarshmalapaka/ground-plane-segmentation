# data_collection.py
"""
Brief: Teleoperates a robot around and records a HD video for a duration of 5 minutes to be used as 
       a datset for training a sematic segmentation Deep Learning model. 
Course: ENPM673 - Perception for Autonomous Robotics [Project-04]
        University of Maryland, College Park (MD)
Date: 25th April, 2022
"""

import os
import time
import RPi.GPIO as gpio
from datetime import datetime
from picamera import PiCamera
from picamera.array import PiRGBArray

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

# Setting up the motor pins on the Motor Driver 
gpio.setup(31, gpio.OUT) # IN1
gpio.setup(33, gpio.OUT) # IN2
gpio.setup(35, gpio.OUT) # IN3
gpio.setup(37, gpio.OUT) # IN4


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


def keyInput(event):
 
    print("Key: ", event)
    key_press = event
    tf = 1    # move bot 1 second
    
    if key_press.lower() == 'w':
        moveForward(tf)
    elif key_press.lower() == 'z':
        moveReverse(tf)
    elif key_press.lower() == 'a':
        rotateLeft(tf)
    elif key_press.lower() == 's':
        rotateRight(tf)
    else:
        print("Invalid key pressed!!")


camera = PiCamera()    # Initialize the PiCamera instance
rawCapture = PiRGBArray(camera)
camera.resolution = (1280, 720)
camera.framerate = 30
camera.rotation = 180    # Camera feed is rotated by 180 deg

camera.start_preview()
file_name = datetime.now().strftime('%Y%m%d%H%M%S')
camera.start_recording("/home/pi/Videos/" + file_name + ".h264")

start_time = time.time()

while True:
    key_press = input("Select the driving mode: ")

    # Stop the bot and recording after 300 seconds (5 minutes) or by pressing 'p' 
    if key_press == 'p' or time.time() - start_time >= 300:
        stopRobot()
        gpio.cleanup()    # Clean up the motor GPIO pins
        break

    keyInput(key_press)

camera.stop_recording()
camera.stop_preview()

# Convert the .h264 video file to .mp4
command = 'MP4Box -add /home/pi/Videos/' + file_name + '.h264 -fps 30 /home/pi/Videos/' + file_name + '.mp4'
os.system(command)
        