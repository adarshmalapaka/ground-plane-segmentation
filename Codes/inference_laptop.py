#Importing Necessary packages
import glob
import os
import torch
import pytorch_lightning as pl
#import matplotlib.pyplot as plt
import segmentation_models_pytorch as smp
import argparse
from torch.utils.data import DataLoader
import time
import cv2
import io
import socket
import struct
import numpy as np
from PIL import Image
from segmentation_models_pytorch.datasets import SimpleOxfordPetDataset
from model import PathModel

"""
@Authors: Sparsh Bhogavilli, Adarsh Malapaka, Kumara Ritvik Oruganti
"""
#argument parser for different versions (if available in logs)
parser = argparse.ArgumentParser()
parser.add_argument('--v', type=int, help='training run in lightning logs folder')
args = parser.parse_args()

mode = "test"
root = '..'
batch_size = 1
n_cpu = os.cpu_count()

#Server run on the laptop/computer to get the images from raspberry pi camera
server_socket = socket.socket()
server_socket.bind(('10.104.48.69', 8000))  # ADD IP HERE
server_socket.listen(0)
connection = server_socket.accept()[0].makefile('rb') #Accept the first connection

#Path to the inference model
PATH = glob.glob('lightning_logs/version_{}/checkpoints/*ckpt'.format(args.v))
assert len(PATH) == 1
model = PathModel.load_from_checkpoint(PATH[0], arch="Unet", encoder_name="resnet18", in_channels=3, out_classes=1, mode=mode)
model.cuda()
#output path
out_path = 'predictions/test'
#Video writer to save the segmented images
video_writer = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Path_Segmentation_Kim3.avi',video_writer,30,(1280,720)) #Path to save the video

if not os.path.exists(out_path):
    os.makedirs(out_path)

try:
    img = None
    prev_frame = 0
    while True:
    
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]

        if not image_len:
            break
        #Image stream object to receive the image from socket connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        
        image_stream.seek(0)

        #image = cv2.cvtColor(np.array(Image.open(image_stream)), cv2.COLOR_RGB2BGR)
        #Converting the received image to the model input size
        image = np.array(Image.open(image_stream))
        image = cv2.resize(image, (640, 352))
        image = cv2.rotate(image, cv2.ROTATE_180)
        orig_img = image.copy()
        orig_img = cv2.cvtColor(orig_img, cv2.COLOR_RGB2BGR)
        image = np.moveaxis(image, -1, 0)
        image = np.expand_dims(image, 0)
       
        #cv2.imshow("Image Receieved from Robot", image)
        #cv2.waitKey(1)
        start_time = time.time()
        #Inference the image
        with torch.no_grad():
            model.eval()
            logits = model(image)
        pr_mask = logits.sigmoid()[0]
        pr_mask = pr_mask.cpu().numpy().squeeze()

        alpha = 0.8 #To overlay mask on the original image
        beta = 1-alpha
        #pr_mask = cv2.cvtColor(pr_mask, cv2.COLOR_GRAY2BGR)
        green_mask = np.ones((352, 640, 3))*255
        green_mask[:,:,0] = 0
        green_mask[:,:,2] = 0
        #orig_img = orig_img.squeeze().transpose(1,2,0)
        pr_mask = pr_mask*128
        green_mask[:,:,1][pr_mask<5] = 0

        print(green_mask.shape, orig_img.shape, type(green_mask), type(orig_img))
        image = cv2.addWeighted(np.uint8(orig_img), alpha, np.uint8(green_mask), beta, 0.0)
        image = cv2.resize(image,(1280,720),interpolation=cv2.INTER_LINEAR) #Resize the image
				
        #print(pr_mask)
        cv2.imshow('prediction', image) #Show the segmented image
        cv2.waitKey(1)
        out.write(image) #Write the image to the video
        fps = batch_size / (time.time() - start_time)
        print('fps:', fps)

#Close all the connections and writer objects
finally:
    connection.close()
    server_socket.close()
    out.release()
