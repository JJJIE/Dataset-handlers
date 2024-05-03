import os
import shutil
from PIL import Image

def convert_and_move_images(source_dir, target_dir, start_num, end_num):
    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_dir, exist_ok=True)

    # 循环指定范围内的图片编号
    for i in range(start_num, end_num + 1):
        # Generate file names using string formatting
        file_name_png = f"{i:06}_seg.png"
        file_name_jpg = f"{i:06}.jpg"
        # file_name_png = f"{i}.png"
        # file_name_jpg = f"{i}.jpg"
        source_file_path = os.path.join(source_dir, file_name_png)
        target_file_path = os.path.join(target_dir, file_name_jpg)

        # Check if the source path is a file, not a directory
        if os.path.isfile(source_file_path):
            # If PNG file exists, read, convert, and save as JPG
            with Image.open(source_file_path) as image:
                rgb_image = image.convert('RGB')  # Convert to RGB mode
                rgb_image.save(target_file_path, 'JPEG')
        else:
            print(f"File not found or is a directory: {source_file_path}")

    print(f"Images from {start_num:05} to {end_num:05} have been converted from PNG to JPG and moved from {source_dir} to {target_dir}.")

# 设置源文件夹和目标文件夹路径
source_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/Downloads/dataset_100000"
target_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/FSGGAN/contaminate/seg"

# 转换并移动
convert_and_move_images(source_folder, target_folder, 1, 90000)

