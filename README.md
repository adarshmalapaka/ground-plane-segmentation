[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Drivable Ground Path Detection Using Semantic Segmentation

Project - 04 for the course, 'ENPM673 - Perception for Autonomous Robots' at the University of Maryland, College Park.

Implementation of detecting the drivable path in the ground plane for a mobile robot in an indoor environment using Semantic Segmentation (U-Net) on a custom collected dataset on the campus of the University of Maryland, College Park.

## Team Members:
* Adarsh Malapaka (amalapak@terpmail.umd.edu)
* Kumara Ritvik Oruganti (okritvik@terpmail.umd.edu)
* Sai Sandeep Adapa (sadapa@umd.edu)
* Sparsh Bhogavilli (sbhogavi@umd.edu)
* Venkata Sai Ram Polina (sairamp@umd.edu)

#### Note: 
Please contact any one of the team members (listed above) to gain access to the dataset, if you're interested!

## Pipeline:
<p align="center">
      <img src="https://user-images.githubusercontent.com/40534801/168429360-9f0d550e-13b6-49d1-9917-34d98a8ec8ef.png" width="80%">
</p>

## Training:
- For details on training & testing the model on a machine with GPU, check out `./Codes/training/usage.md` file - [link](https://github.com/adarshmalapaka/ground-plane-segmentation/blob/main/Codes/training/usage.md).

## Model Results:

### Training Curves

Train Loss v/s Epoch    |  Train IOU v/s Epoch |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168428961-2c033e76-cc1c-4369-85c5-62d0e5b3ea99.png" width="90%"> | <img src="https://user-images.githubusercontent.com/40534801/168428928-c37d4d93-c065-4002-8ebd-4b75b6522282.png" width="90%"> 

Validation Loss v/s Epoch    |  Validation IOU v/s Epoch |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168428991-ceec26e5-aed2-4878-9afa-50297e43de7e.png" width="90%"> | <img src="https://user-images.githubusercontent.com/40534801/168428974-ed50f9d6-4c23-4d05-ae7d-155892d6449e.png" width="90%"> 


### Cross-Validation

| Metric        | Fold-1           | Fold-2           | Fold-3           | Average           |
| ------------- |:----------------:|:----------------:|:----------------:|:-----------------:|
| Test IOU      | 0.998            | 0.998            | 0.999            | 0.9983            | 


### Test Results

#### Videos
<p align="center">
<a href="https://youtu.be/tdF0aCcTwDY" target="_blank">
 <img src="http://img.youtube.com/vi/tdF0aCcTwDY/mqdefault.jpg" alt="Watch the video" width="350" height="200" border="10" />
</a>
</p>

<p align="center">
<a href="https://youtu.be/34u9Obz_LbE" target="_blank">
 <img src="http://img.youtube.com/vi/34u9Obz_LbE/mqdefault.jpg" alt="Watch the video" width="350" height="200" border="10" />
</a>
</p>


#### Test results on Laptop
<p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/168428335-ba6d5099-b896-4456-989c-52e5f2736489.png" width="80%">
 </p>
<p align="center">
The pillar is classified as Non-drivable
</p>

#### Deploying on Mobile Robot
- A camera is mounted on a mobile robot platform & its stream is transferred to a laptop using RaspberryPi.
- On the laptop, semantic segmentation to detect drivable path is done by running the command `python3 inference_laptop.py` from the folder `./Codes`.
- The below images are two samples of the same.
- [Here](https://youtu.be/34u9Obz_LbE) and [here](https://youtu.be/tdF0aCcTwDY) are the video links of the model inferencing from laptop using the camera stream from robot. 

Detected Ground (Feet labeled as non-drivable)   |  Detected Ground (Floor-mat labeled as drivable) |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168384097-9191c43b-489d-45aa-9bf9-004601714acf.jpeg" width="70%"> | <img src="https://user-images.githubusercontent.com/40534801/168384728-e9b04c0b-0843-4484-a711-4cd589703f54.jpeg" width="70%"> 

#### Testing on Jetson TX2
<p align="center">
        <img src="https://user-images.githubusercontent.com/40200916/168886921-54bb66d2-192d-4da8-83fb-e1354b50e6fd.png" width = 100%>
</p>

## Dataset:
 
### Locations
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/168385268-8721eca2-483d-4771-bc03-8014817b0a3f.jpg" width="550" height="300">
  </p>

<details>
<summary>Key for Depicted Locations (with number of videos recorded)</summary>
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

### Collection Methodology

 Robot for Data Collection    |  Data Collection in Martin Hall |
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/40534801/168385473-9119bcf1-fa4e-4302-af1a-4d26837d4262.jpeg" width="40%"> | <img src="https://user-images.githubusercontent.com/40534801/168385504-5f915cdd-ff47-4ac3-909a-8bd61fdbc515.jpeg" width="50%"> 

### Video Specifications
* Resolution: 1280 x 720 (16:9 ratio)
* Video Duration: 5 minutes
* Framerate: 30
* Height of Camera: 12 cm approx (from the ground)

Every 100th frame of each video was saved as an image for the dataset (1260 dataset images)
