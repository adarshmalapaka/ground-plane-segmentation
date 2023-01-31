[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Drivable Ground Path Detection Using Semantic Segmentation

This repository holds the implementation of detecting the drivable path in the ground plane for a mobile robot in an indoor environment. A U-Net based Semantic Segmentation model is trained on a custom dataset collected on the campus of the University of Maryland, College Park. This project is done as part of the course 'ENPM673 - Perception for Autonomous Robots' at the University of Maryland, College Park.


## Team Members:
* Adarsh Malapaka* (amalapak@terpmail.umd.edu)
* Kumara Ritvik Oruganti* (okritvik@terpmail.umd.edu)
* Sparsh Bhogavilli* (sbhogavi@terpmail.umd.edu)
* Sai Sandeep Adapa (sadapa@umd.edu)
* Venkata Sai Ram Polina (sairamp@umd.edu)

#### Note:
- \* Denotes equal contribution.
- Please contact any one of the team members (listed above) to gain access to the [dataset](https://drive.google.com/drive/folders/16BNODe_qVlgKhFiYIx_n6eobk5GPRHp9?usp=sharing), if you're interested!

## Pipeline:
<p align="center">
      <img src="https://user-images.githubusercontent.com/40534801/168429360-9f0d550e-13b6-49d1-9917-34d98a8ec8ef.png" width="80%">
</p>

## Training:
- Check out the [usage.md](https://github.com/adarshmalapaka/ground-plane-segmentation/blob/main/Code/training/usage.md) for details on training & testing the model on a machine with a CUDA enabled GPU.

### Training Curves

Train Loss v/s Epoch    |  Train IOU v/s Epoch |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168428961-2c033e76-cc1c-4369-85c5-62d0e5b3ea99.png" width="90%"> | <img src="https://user-images.githubusercontent.com/40534801/168428928-c37d4d93-c065-4002-8ebd-4b75b6522282.png" width="90%"> 

Validation Loss v/s Epoch    |  Validation IOU v/s Epoch |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168428991-ceec26e5-aed2-4878-9afa-50297e43de7e.png" width="90%"> | <img src="https://user-images.githubusercontent.com/40534801/168428974-ed50f9d6-4c23-4d05-ae7d-155892d6449e.png" width="90%"> 



## Testing
### Test results on Laptop
- The model is 3-fold Cross-Validated & the following are the results.

#### 3-Fold Cross-Validated Test IOU
| Metric        | Fold-1           | Fold-2           | Fold-3           | Average           |
| ------------- |:----------------:|:----------------:|:----------------:|:-----------------:|
| Test IOU      | 0.998            | 0.998            | 0.999            | 0.9983            | 

#### Visualization
- The following image shows the segmentation output on an image from the test set.
<p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/168428335-ba6d5099-b896-4456-989c-52e5f2736489.png" width="80%">
 </p>
<p align="center">
It can be observed that the pillar is classified as Non-drivable region.
</p>

### Deploying on Mobile Robot
- A camera has been mounted on a mobile robot platform and a Raspberry Pi, which is integrated into the platform, is utilized to transmit the camera's video stream to a laptop computer.
- Inference is then conducted on the video stream on the laptop using the [inference_laptop.py](https://github.com/adarshmalapaka/ground-plane-segmentation/blob/main/Code/inference_laptop.py) script.
- The below two images are samples of the same.

Detected Ground (Feet labeled as non-drivable)   |  Detected Ground (Floor-mat labeled as drivable) |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168384097-9191c43b-489d-45aa-9bf9-004601714acf.jpeg" width="70%"> | <img src="https://user-images.githubusercontent.com/40534801/168384728-e9b04c0b-0843-4484-a711-4cd589703f54.jpeg" width="70%"> 

#### Demo Videos
- 3rd-person Point-of-View of Mobile Robot transmitting video stream from a corridor & inference on laptop (in top-left)
<p align="center">
<a href="https://youtu.be/34u9Obz_LbE" target="_blank">
 <img src="http://img.youtube.com/vi/34u9Obz_LbE/mqdefault.jpg" alt="Video of Inferencing Segmentation of Drivable Path in J M Patterson Hall, UMD" width="350" height="200" border="10" />
</a>
</p>

- Laptop screen capture of inference being run on video stream received from the robot.
<p align="center">
<a href="https://youtu.be/tdF0aCcTwDY" target="_blank">
 <img src="http://img.youtube.com/vi/tdF0aCcTwDY/mqdefault.jpg" alt="Watch the video" width="350" height="200" border="10" />
</a>
</p>


### Testing on Jetson TX2
- The learned PyTorch model was converted to ONNX format on the laptop & then to TensorRT engine on a Jetson TX2 platform.
- The following is the terminal output of successful TensorRT conversion.
<p align="center">
        <img src="https://user-images.githubusercontent.com/40200916/168886921-54bb66d2-192d-4da8-83fb-e1354b50e6fd.png" width = 100%>
</p>


## Dataset:
- The dataset used for this project is made from the videos collected from the following locations on the University of Maryland's College Park campus.

  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/168385268-8721eca2-483d-4771-bc03-8014817b0a3f.jpg" width="550" height="300">
  </p>
<details>
<summary>Drop-down menu: Key for Depicted Locations (with number of videos recorded)</summary>
<p align="center"> 1. Atlantic Bldg (1 video) </p>
<p align="center"> 2. J.M. Patterson Bldg (2 videos) </p>
<p align="center"> 3. Chem/Nuclear Bldg (1 video) </p>
<p align="center"> 4. A.V. Williams Bldg (1 video) </p>
<p align="center"> 5. Brendan Iribe Center (1 video) </p>
<p align="center"> 6. Glenn Martin Hall (2 videos) </p>
<p align="center"> 7. Plant Sciences Bldg (1 video) </p>
<p align="center"> 8. Psychology/Biology Bldg (1 video) </p>
<p align="center"> 9. Symons Hall (1 video) </p>
<p align="center"> 10. Woods Hall (1 video) </p>
<p align="center"> 11. Tydings Hall (1 video) </p>
<p align="center"> 12. Lefrak Hall (1 video) </p>
</details>
  
&nbsp;

### Collection Methodology
 Robot used for Data Collection    |  Data Collection in Glenn Martin Hall |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168385473-9119bcf1-fa4e-4302-af1a-4d26837d4262.jpeg" width="40%"> | <img src="https://user-images.githubusercontent.com/40534801/168385504-5f915cdd-ff47-4ac3-909a-8bd61fdbc515.jpeg" width="50%"> 

### Video Specifications
* Resolution: 1280 x 720 (16:9 ratio)
* Video Duration: 5 minutes
* Framerate: 30fps
* Height of Camera: 12 cm approx (from the ground)

### Image extraction
- Every 100th frame of each video was extracted to form a total of 1260 images in the dataset.

### Data Annotation
- The tool [Dataloop](https://dataloop.ai/) is used for annotating the ground truth masks on the images.

### Data Augmentation
- Data Augmentation techniques like Random crop, Horizontal flip & brightness changes are used.