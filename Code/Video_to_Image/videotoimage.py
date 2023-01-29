#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kumara Ritvik Oruganti and Sairam Polina
"""
#Import opencv package
import cv2
import os
#Get the path of the videos
path=os.getcwd()+'\Videos'
videos = os.listdir(path)
print(videos)
image_count=1 #For saving the image with file name
video_id = 64 #Encoding the videos with alphabets
for video_name in videos:
    video_path=path+'\\'+video_name #path for the videos to be divided into frames
    save_path=os.getcwd()+'\Data\\' #Path to save the images
    # print(save_path)
    vobj=cv2.VideoCapture(video_path) #video object
    video_id += 1 #Incrementing the Video ID
    if vobj.isOpened()==False:
        print("Error Loading the video")
    #Frame count
    frame_no=0
    print("Video Name: ",video_name, " Corresponding Code: ",str(chr(video_id)))
    while vobj.isOpened():

        res,frame=vobj.read()

        frame_no+=1 #Increment the frame count if a frame is read from the video


        if res==True:

            # cv2.imshow('Final Project Data',frame)
            # cv2.waitKey(2)

            if frame_no==100: #Save every 100th frame

                image_string=str(image_count)
                name=str(chr(video_id))+image_string.zfill(5)
                cv2.imwrite(save_path+name+'.png', frame)
                # re-assign frame_no and image_count
                frame_no=0
                image_count+=1 #Increment the image count

            # if cv2.waitKey(2)==ord('q'):
            #     break
        else:
            break
# cv2.destroyAllWindows()
#uncomment 35,36,47,48,51 lines to visualize the frames read from the video