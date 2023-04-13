import os
import shutil
import glob
from math import ceil
from itertools import product
from random import shuffle

src_folder = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_align_celeba'
train_ratio = 0.8
images_per_folder = 3000

# 获取字母表，用于生成子文件夹名
alphabet = 'abcdefghijklmnopqrstuvwxyz'
folder_names = [''.join(combination) for combination in product(alphabet, repeat=2)]

all_images = glob.glob(os.path.join(src_folder, '*.jpg'))
shuffle(all_images)

total_images = len(all_images)
train_size = int(train_ratio * total_images)

train_images = all_images[:train_size]
val_images = all_images[train_size:]

os.makedirs(os.path.join(src_folder, 'train'))
os.makedirs(os.path.join(src_folder, 'val'))

def move_images_to_folders(images, parent_folder):
    folder_idx = 0
    for idx, image_path in enumerate(images):
        if idx % images_per_folder == 0:
            folder_name = folder_names[folder_idx]
            folder_idx += 1
            os.makedirs(os.path.join(parent_folder, folder_name))

        filename = os.path.basename(image_path)
        shutil.move(image_path, os.path.join(parent_folder, folder_name, filename))

move_images_to_folders(train_images, os.path.join(src_folder, 'train'))
move_images_to_folders(val_images, os.path.join(src_folder, 'val'))
