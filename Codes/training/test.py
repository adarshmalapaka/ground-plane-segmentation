import os
import torch
import argparse
import time
import cv2
import numpy as np
from PIL import Image
from model import PathModel

parser = argparse.ArgumentParser()
parser.add_argument('--m', type=str, help='Path to the trained model relative to cwd')
parser.add_argument('--i', type=str, help='Path to the image to be tested on')
args = parser.parse_args()

mode = "test"
batch_size = 1
n_cpu = os.cpu_count()

PATH = args.m
img_path = args.i
assert os.path.exists(PATH), "model isn't present at {}".format(PATH)
assert os.path.exists(img_path), "image isn't present at {}".format(PATH)
model = PathModel.load_from_checkpoint(PATH, arch="Unet", encoder_name="resnet18", in_channels=3, out_classes=1, mode=mode)
model.cuda()

out_path = 'predictions/test/'
if not os.path.exists(out_path):
    os.makedirs(out_path)

image = np.array(Image.open(img_path))
image = cv2.resize(image, (640, 352))
orig_img = image.copy()
orig_img = cv2.cvtColor(orig_img, cv2.COLOR_RGB2BGR)
image = np.moveaxis(image, -1, 0)
image = np.expand_dims(image, 0)

start_time = time.time()
with torch.no_grad():
    model.eval()
    logits = model(image)
pr_mask = logits.sigmoid()[0]
pr_mask = pr_mask.cpu().numpy().squeeze()

alpha = 0.8
beta = 1-alpha
green_mask = np.ones((352, 640, 3))*255
green_mask[:,:,0] = 0
green_mask[:,:,2] = 0
pr_mask = pr_mask*128
green_mask[:,:,1][pr_mask<5] = 0

image = cv2.addWeighted(np.uint8(orig_img), alpha, np.uint8(green_mask), beta, 0.0)

fps = batch_size / (time.time() - start_time)
print('fps:', fps)

cv2.imshow('prediction', image)
cv2.waitKey(0)
cv2.imwrite(out_path+img_path.split('/')[-1], image)
