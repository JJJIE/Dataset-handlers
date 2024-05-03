import os
import shutil


def copy_first_n_files(source_dir, target_dir, n=300):
    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_dir, exist_ok=True)

    # 获取所有文件
    files = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    # 按文件名排序
    files.sort()

    # 仅选择前n个文件
    files_to_copy = files[:10000]

    # 复制文件
    for filename in files_to_copy:
        shutil.copy(os.path.join(source_dir, filename), os.path.join(target_dir, filename))

    print(f"Copied {len(files_to_copy)} files from {source_dir} to {target_dir}.")


# 设置源文件夹和目标文件夹路径
source_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/Downloads/dataset_100000"  # 替换为你的源文件夹路径
target_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/test"  # 替换为你的目标文件夹路径

files = [file for file in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file))]
print(f"Total files in source directory: {len(files)}")
# 复制前10000个文件
copy_first_n_files(source_folder, target_folder)
