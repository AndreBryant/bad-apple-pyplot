import cv2
import matplotlib.pyplot as plt
from glob import glob
import os

def get_black_px(bin_img): 
    black_px = []
    for x in range(bin_img.shape[0]):
        for y in range(bin_img.shape[1]):
            if bin_img[x,y] == 0:
                black_px.append((x,y))
    return black_px

imgs = sorted(glob('.\\img\\360p_bad_apple\\*.png'), key= lambda x: int(x.split('\\')[-1].split('_')[-1].split('.')[0]))
img_len = len(imgs) - 1

fig, ax = plt.subplots()

output_dir = '.\\render\\frames\\'
os.makedirs(output_dir, exist_ok=True)

for i, img_path in enumerate(imgs):
    ax.clear()

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    _, bin_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    black_px = get_black_px(bin_img)
    x = [-x[0] for x in black_px]
    y = [y[1] for y in black_px]

    ax.scatter(y, x, s=0.1, color='#000')
    ax.set_title(f"frame {i:04d}")

    filename = f"frame_{i:04d}.png"
    print(f"{i:04d}/{img_len}")

    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path)
    
plt.close()

os.system("ffmpeg -framerate 30 -i ./render/frames/frame_%04d.png -i ./img/bad_apple.wav -c:v libx264 -pix_fmt yuv420p ./render/output.mp4")

for i in range(len(img)-1):
    os.remove(f'./render/frames/frame_{i:04d}.png')

