import os
import shutil


def move_specific_images(source_dir, target_dir, start_num, end_num):
    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_dir, exist_ok=True)

    # 循环指定范围内的图片编号
    for i in range(start_num, end_num + 1):
        file_name = f"{i}.jpg"
        source_file_path = os.path.join(source_dir, file_name)
        target_file_path = os.path.join(target_dir, file_name)

        # 如果文件存在，则移动，否则打印不存在的文件名
        # if os.path.exists(source_file_path):
        #     shutil.move(source_file_path, target_file_path)
        # else:
        #     print(f"File not found: {file_name}")

        # 如果文件存在，则复制，否则打印不存在的文件名
        if os.path.exists(source_file_path):
            shutil.copy(source_file_path, target_file_path)
        else:
            print(f"File not found: {file_name}")

    print(f"Images from {start_num}.jpg to {end_num}.jpg have been moved from {source_dir} to {target_dir}.")


# 设置源文件夹和目标文件夹路径
source_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_celeba_hq"
target_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/FSGGAN/celeba_rand_test/celeba_rand_test"

# 移动0.jpg 到 2999.jpg
move_specific_images(source_folder, target_folder, 27000, 29999)
