import cv2
import numpy as np
#Importing ONNX Runtime package to run the generic model on the GPU cores
import onnxruntime as rt
from numpy import expand_dims
from numpy import asarray
from PIL import Image
from numpy import moveaxis
import time
"""
@Author: Kumara Ritvik Oruganti
"""
#Create an inference session
sess = rt.InferenceSession("detection_model.onnx",providers=['TensorrtExecutionProvider', 'CUDAExecutionProvider'])

#Test Video
video = cv2.VideoCapture('20220426110252.mp4')

init_time = time.time()
#While the video is not closed
while(video.isOpened()):
    #Read the image
	ret,frame = video.read()
	if ret:
        #Count the time taken to inference for getting the FPS
        
		start_time = time.time()
        #Resize for the model input
		frame = cv2.resize(frame,(640,352))
        
		#cv2.imshow("Original Frame",frame)
		#print(frame.shape)
		
        #Convert the BGR image to RGB
        frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		#Convert to PILarray
        frame = Image.fromarray(frame)
        
        
		#cv2.imshow("Original Frame",frame)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
        
        #Convert to numpy array
		frame = asarray(frame)
		#print(frame.shape)
           
        #Change the RGBC to HWC to CWH
		frame =  moveaxis(frame,1,2)
		frame =  moveaxis(frame,0,1)
		#print(frame.shape)
        
        #Convert from uint8 to float32
		frame  =  frame[np.newaxis,  ...].astype(np.float32)
        
        #Inference session inputs and outputs
		output_name = sess.get_outputs()[0].name
		input_name = sess.get_inputs()[0].name

		#print("Output Name ",sess.get_outputs()[0])
		#print("Input Name ",input_name)
        
        #Detect the path from the frame
		detections = sess.run([output_name], {input_name: frame})[0]
		#print("Output Shape",detections)
		#print(detections[0].shape)
        
        #Convert the detections from tensor format to uint8 for the image visualization
		detected = np.uint8(detections[0])
		#print("Original Detection Shape: ",detected.shape)
        
        #Convert the CWH to HWC
		detected = moveaxis(detected,0,1)
		detected = moveaxis(detected,1,2)
		#detected = cv2.flip(detected, 0)
        
        #Output the mask
		cv2.imshow("Output",detected)
		cv2.waitKey(1)
        
        #Print the detected mask
		print("FPS: ",(1.0)/(time.time()-start_time))
	else:
		break
#cv2.waitKey(0)
end_time = time.time()

total_time = end_time - init_time
print("Total Time: ",total_time)
print("Average FPS: ",9000/total_time)
cv2.destroyAllWindows()
