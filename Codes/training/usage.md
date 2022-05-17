# Requirements 
- `pip install segmentation-models-pytorch`
- `pip install pytorch-lightning==1.5.4`
- `pip install opencv-python`
- Please resolve any dependencies issues that might occur while running the code.

# Usage:
- First, change the working directory to `<root>/Codes/training` folder.
## Testing:
- Download the trained model from [here](https://drive.google.com/file/d/1j2hYuX1fm-atKk3rfyfeMeRtN4N1duY8/view?usp=sharing) & move it to `<root>/Codes/training/trained_models` folder.
- To test the trained model with any random image: `python3 test.py --m=./trained_models/trained_model.ckpt --i=./data/orig_imgs/A00019.png`
- Replace the `--i` tag with your desired image & play around!
- The predicted output is saved to `./predictions/test` folder
## Training:
- `python3 train.py --fold=1`
## .ckpt to .onnx conversion:
- To convert ckpt file to onnx file use: `python3 ckpt_to_onnx.py`.

# Dataset:
- The images intended to be used for training, validation & testing are to be kept in `data/orig_imgs` folder.
- The annotation masks (ground truth) are to be kept in `data/annotated_data` folder.
- Binary masks for the same are to be kept in `data/bin_masks` folder. They can be generated from the above annotations by running `python3 gen_bin_masks.py` command from the `<root>/Codes/training/data` folder.
- The train, valid & test splits are to be made & the file names are to be kept in `data/{train,valid,test}_fold1.txt` files.

# Note:
- It is recommended that the aspect-ratio in which the test image is captured is close to 16:9.
- For illustrative prposes, a toy dataset (with 1 image each for train, validation & test sets) is provided in `data` folder. The actual full dataset on which the model is trained can be accessed by contacting the authors.

# Acknowledgement
- The training code is taken from [this repo](https://github.com/qubvel/segmentation_models.pytorch) & customized to our problem.
