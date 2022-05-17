import torch
from model import PathModel
import numpy as np

batch_size = 8
# Input to the model
x =  torch.rand(batch_size, 3, 352, 640, requires_grad=True)

PATH = './trained_models/trained_model.ckpt'
out_path = PATH[:-5]+'.onnx'
torch_model = PathModel.load_from_checkpoint(PATH, arch="Unet", encoder_name="resnet18", in_channels=3, out_classes=1)

torch_model.eval()
torch_out = torch_model(x)

# Export the model
torch.onnx.export(torch_model,               # model being run
                  x,                         # model input (or a tuple for multiple inputs)
                  out_path,                  # where to save the model (can be a file or file-like object)
                  export_params=True,        # store the trained parameter weights inside the model file
                  opset_version=11,          # the ONNX version to export the model to
                  do_constant_folding=True,  # whether to execute constant folding for optimization
                  input_names = ['input'],   # the model's input names
                  output_names = ['output'], # the model's output names
                  dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                                'output' : {0 : 'batch_size'}})
