import os
import shutil

# 定义文件夹路径
image_path = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/images_ori_part/"  # 替换为实际的image文件夹路径
lab_path = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/labels_ori/"  # 替换为实际的lab文件夹路径
new_folder_path = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/labels/"  # 替换为希望存放复制文件的新文件夹路径

# 如果新文件夹不存在，则创建它
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    print(f"Created new folder at {new_folder_path}")

# 从 image 文件夹中的文件名中移除 '.jpg.npy' 后缀，并只保留前两个部分
# image_files = ['-'.join(f.replace('.jpg', '').split('-')[:2]) for f in image_files_raw]

# 从 lab 文件夹中的文件名中移除 '.png' 后缀，并只保留前两个部分
# lab_files = ['-'.join(f.replace('.pkl', '').split('-')[:2]) for f in lab_files_raw]

# 找出lab中与image文件夹同名的文件名
# to_copy = set(image_files) & set(lab_files)

# 列出文件夹中的文件名
image_files_raw = [os.path.splitext(f)[0] for f in os.listdir(image_path) if f.endswith('.jpg')]  # 获取不包含后缀的文件名列表
lab_files_raw = [f for f in os.listdir(lab_path) if f.endswith('.png')]

# 找出lab中与image文件夹同名的文件名
to_copy = set(image_files_raw) & set([os.path.splitext(f)[0] for f in lab_files_raw])

print(f"Found {len(to_copy)} common files to copy")

# 复制这些文件到新文件夹
for name in to_copy:
    source_file = os.path.join(lab_path, name + ".png")
    dest_file = os.path.join(new_folder_path, name + ".png")
    shutil.copy2(source_file, dest_file)
    print(f"Copied {name}.pkl to the new folder")

print("Operation completed!")



