import cv2
from glob import glob

images = glob('annotated_data/*/*path.png')
images.sort()

for img_pth in images:
    img = cv2.imread(img_pth)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img != 0] = 1
    cv2.imwrite('bin_masks/'+img_pth.split('/')[-1].split(' ')[0]+'.png', img)
