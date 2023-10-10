import os
import shutil

# 定义源文件夹和目标文件夹
src_folder = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_segme_tv/val/b'   # a-h
dst_folder = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_label'

# 确保目标文件夹存在，如果不存在则创建
os.makedirs(dst_folder, exist_ok=True)

# 遍历源文件夹中的所有文件

for filename in os.listdir(src_folder):
    # 获取文件完整路径
    src_path = os.path.join(src_folder, filename)
    dst_path = os.path.join(dst_folder, filename)

    # 复制文件
    shutil.copy(src_path, dst_path)
