import os
import cv2
from glob import glob

imgs = glob('.\\img\\image_sequence\\*.png')
output_dir = '.\\img\\low-res-bad-apple\\'
os.makedirs(output_dir, exist_ok=True)

# 1080p: 1440, 1080
# 720p: 1280, 720
# 360p: 640, 360 
# xp: 1.77777x, x

for img_path in imgs:
    img = cv2.imread(img_path)
    img_prime = cv2.resize(img, (640, 360))
    filename = os.path.split(img_path)[-1]
    print(filename)

    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, img_prime)