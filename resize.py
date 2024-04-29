import os
from PIL import Image

def resize_images(directory, width, height):
    # 遍历指定目录下的所有文件
    files = [file for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for filename in files:
        file_path = os.path.join(directory, filename)  # 获取文件完整路径
        with Image.open(file_path) as img:
            img = img.resize((width, height))  # 调整图片大小
            img.save(file_path)  # 保存调整后的图片

# 使用示例
directory_path = '/path/to/your/directory'  # 替换为你的文件夹路径
new_width = 0  # 设置新的宽度
new_height = 0  # 设置新的高度

resize_images(directory_path, new_width, new_height)
