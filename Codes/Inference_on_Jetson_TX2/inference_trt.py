import os
#Import the tensorrt to run the trt engine on the GPU Cuda and Tensor Cores
import tensorrt as trt

#importing cuda drivers and packages for python
import pycuda.autoinit
import pycuda.driver as cuda
import cv2
import time
import numpy as np

#import the numpy and PIL packages to convert the image to required model input
from numpy import expand_dims
from numpy import asarray
from PIL import Image
from numpy import moveaxis

"""
@Author: Kumara Ritvik Oruganti
"""

#Host and Cuda Inputs
host_inputs  = []
cuda_inputs  = []

#Host and Cuda Outputs
host_outputs = []
cuda_outputs = []

#Bindings
bindings = []


def load_engine(trt_runtime, engine_path):
    '''
    This functions loads the TRT engine of the inferencing model
    @param trt_runtime: Tensor RT Runtime Logger
    @param engine_path: TRT engine file path
    '''
    with open(engine_path, 'rb') as f:
        engine_data = f.read()
    
    #Deserialize the cuda engine from the trt engine
    engine = trt_runtime.deserialize_cuda_engine(engine_data)
    
    for binding in engine:
            size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size #here the batch size is taken dynamically from the model while generating the tensorrt engine
            
            host_mem = cuda.pagelocked_empty(shape=[size],dtype=np.float32)
            cuda_mem = cuda.mem_alloc(host_mem.nbytes) #allocate the image size memory in cuda

            bindings.append(int(cuda_mem)) #Add the memory in bindings
            if engine.binding_is_input(binding):
                host_inputs.append(host_mem)
                cuda_inputs.append(cuda_mem)
            else:
                host_outputs.append(host_mem)
                cuda_outputs.append(cuda_mem)

    return engine #return the deserialized cuda engine


TRT_LOGGER = trt.Logger(trt.Logger.WARNING) #Tensor RT logger (Set to warning)
trt_runtime = trt.Runtime(TRT_LOGGER) #Runtime object
trt_engine_path = "ground_model.trt" #Engine path
engine = load_engine(trt_runtime, trt_engine_path) #Get the deserialized cuda engine
video = cv2.VideoCapture('20220426110252.mp4') #Test video file path

#Till the video is open
while(video.isOpened()):
    #Read the frame
	ret,image = video.read()
	if ret:	
            start_time = time.time()
            #Resize to required model input size
            image = cv2.resize(image,(640,352))
            #Convert the BGR image to RGB image
            image  = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #convert the cv2 image to the PIL image
            image = Image.fromarray(image)
            #cv2.imshow("Original image",image)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #Convert the PIL array to numpy array
            image = asarray(image)
            #print(image.shape)
            #Change the format of the HWC to CWH
            image =  moveaxis(image,1,2)
            image =  moveaxis(image,0,1)
            #print(image.shape)
            #convert the uint8 to float32 data
            image  =  image[np.newaxis,  ...].astype(np.float32)
            
            #copy the image to input host 
            np.copyto(host_inputs[0], image.ravel())
            #create a cuda stream object
            stream = cuda.Stream()
            #create an execution context
            context = engine.create_execution_context()
            
            cuda.memcpy_htod_async(cuda_inputs[0], host_inputs[0], stream)
            context.execute_async(bindings=bindings, stream_handle=stream.handle)
            cuda.memcpy_dtoh_async(host_outputs[0], cuda_outputs[0], stream)
            stream.synchronize() #Synchronize the stream
            #print("execute times "+str(time.time()-start_time))
            
            #Get the output
            output = host_outputs[0].reshape(np.concatenate(([1],engine.get_binding_shape(1))))[0]
            #print(output.shape)
            
            #Uncomment below to get the mask output and vizualisation
            #detected = np.uint8(output[0])
            #print("Original Detection Shape: ",detected.shape)
            #detected = moveaxis(detected,0,1)
            #detected = moveaxis(detected,1,2)
            #detected = cv2.flip(detected, 0)
            #Print the fps
            print("FPS: ",(1.0)/(time.time()-start_time))
            #cv2.imshow("Output",detected)
            #cv2.waitKey(1)
            
            
cv2.destroyAllWindows()
#print(detected.shape)
        
