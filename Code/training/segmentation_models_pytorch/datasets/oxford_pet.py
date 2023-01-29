import os
import torch
import shutil
import numpy as np
import torch

from PIL import Image
from tqdm import tqdm


class OxfordPetDataset(torch.utils.data.Dataset):
    def __init__(self, root, mode="train", transform=None):

        assert mode in {"train_fold1", "valid_fold1", "test_fold1"}

        self.root = root
        self.mode = mode
        self.transform = transform

        self.images_directory = os.path.join(self.root, 'data', "orig_imgs")
        self.masks_directory = os.path.join(self.root, 'data', "bin_masks")

        self.filenames = self._read_split()  # read train/test splits

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):

        filename = self.filenames[idx]
        image_path = os.path.join(self.images_directory, filename)
        mask_path = os.path.join(self.masks_directory, filename)

        image = np.array(Image.open(image_path).convert("RGB"))

        mask = np.array(Image.open(mask_path))
        mask = self._preprocess_mask(mask)

        sample = dict(image=image, mask=mask, filename=filename)
        if self.transform is not None:
            sample = self.transform(**sample)

        return sample

    @staticmethod
    def _preprocess_mask(mask):
        mask = mask.astype(np.float32)
        return mask

    def _read_split(self):
        split_filename = self.mode+".txt"
        split_filepath = os.path.join(self.root, "data", split_filename)
        with open(split_filepath) as f:
            split_data = f.read().strip("\n").split("\n")
        filenames = split_data
        return filenames


class SimpleOxfordPetDataset(OxfordPetDataset):
    def __getitem__(self, *args, **kwargs):

        sample = super().__getitem__(*args, **kwargs)
        
        # resize images
        resize_w_h = (640, 352)
        image = np.array(Image.fromarray(sample["image"]).resize(resize_w_h, Image.LINEAR))
        mask = np.array(Image.fromarray(sample["mask"]).resize(resize_w_h, Image.NEAREST))
        # convert to other format HWC -> CHW
        sample["image"] = np.moveaxis(image, -1, 0)
        sample["mask"] = np.expand_dims(mask, 0)
        
        # if 'test' in self.mode:
        #     sample["image"] = torch.from_numpy(sample["image"])
        #     sample["mask"] = torch.from_numpy(sample["mask"])
        return sample


class TqdmUpTo(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)
