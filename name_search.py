import os
import shutil
import pickle

# 从pkl文件中加载文件名列表
with open('/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/train_list.pkl', 'rb') as file:
    names_from_pkl = pickle.load(file)

# 设置image文件夹的路径和目标文件夹的路径
image_folder_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/images_ori/'
destination_folder_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/celebID/images_ori_part/'

# 如果目标文件夹不存在，则创建
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# 遍历image文件夹中的所有文件
for filename in os.listdir(image_folder_path):
    # 判断文件是否为jpg格式
    if filename.endswith(".jpg"):
        # 分割文件名，忽略后面的数字
        base_name = '-'.join(filename.split('-')[:-1])
        # 如果base_name在pkl文件中，则复制到目标文件夹
        if base_name in names_from_pkl:
            src_path = os.path.join(image_folder_path, filename)
            dest_path = os.path.join(destination_folder_path, filename)
            shutil.copy2(src_path, dest_path)

print("Files copied successfully!")
