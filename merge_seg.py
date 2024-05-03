import os
from PIL import Image
import numpy as np

# 特征列表和对应的灰度值
features = {
    'background': 0,
    'skin': 1,
    'nose': 2,
    'r_eye': 3,
    'l_eye': 4,
    'r_brow': 5,
    'l_brow': 6,
    'r_ear': 7,
    'l_ear': 8,
    'mouth': 9,
    'u_lip': 10,
    'l_lip': 11,
    'neck': 12,
    'hair': 13,
    'beard': 14,
    'cloth': 15,
    'eye_g': 16,
    'hat': 17,
    'facewear': 18,
    'ear_r': 19,
    'neck_l': 20,
    'ignore': 255
}

# 设定图像大小
size = (512, 512)

# 路径设置
base_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/CelebAMask-HQ/CelebAMask-HQ-mask-anno'  # 修改为您图像所在的目录路径
output_path = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/gray018'  # 修改为输出目录路径

# 创建输出目录
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 收集所有文件及其路径
image_dict = {}
for i in range(15):  # 从0到14的子文件夹
    folder_path = os.path.join(base_path, str(i))
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.png'):
                # 提取编号部分
                file_id = file.split('_')[0]
                full_path = os.path.join(folder_path, file)
                if file_id not in image_dict:
                    image_dict[file_id] = []
                image_dict[file_id].append(full_path)

# 处理收集到的每个编号的图像
for file_id, paths in image_dict.items():
    # 初始化一个全黑的数组
    combined_image = np.zeros(size, dtype=np.uint8)
    for img_path in paths:
        # 提取文件名中的特征部分
        feature_key = img_path.split('_')[-1].split('.')[0].split('/')[-1]
        if feature_key in features:
            img = Image.open(img_path).convert('L')
            img_array = np.array(img)
            # 将特征的灰度值应用到图像上
            combined_image[img_array > 0] = features[feature_key]

    # 保存合并后的图像
    output_filename = os.path.join(output_path, f'{file_id}.png')
    Image.fromarray(combined_image).save(output_filename)
    print(f'Saved combined image to {output_filename}')