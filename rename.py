import os


def rename_images(source_dir, start_old, end_old, start_new):
    # 计算起始的新文件名与旧文件名的差值
    offset = start_new - start_old

    # 遍历指定范围内的所有旧文件名
    for old_index in range(start_old, end_old + 1):
        old_filename = f"{old_index}.jpg"
        new_filename = f"{old_index + offset}_seg.jpg"
        old_file_path = os.path.join(source_dir, old_filename)
        new_file_path = os.path.join(source_dir, new_filename)

        # 如果旧文件存在，则重命名
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_filename} to {new_filename}")
        else:
            print(f"File {old_filename} not found")


def rename_gt(source_folder, start_number, end_number):
    # 获取文件夹内所有图片文件
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]

    # 确保图片数量与新命名范围相匹配
    if len(image_files) > (end_number - start_number + 1):
        print("错误：图片数量超过了指定的命名范围！")
    else:
        # 重命名图片
        for i, filename in enumerate(image_files):
            new_filename = f'{start_number + i:06}.jpg'  # 格式化为六位数，例如 090001, 090002, ...
            old_file_path = os.path.join(source_folder, filename)
            new_file_path = os.path.join(source_folder, new_filename)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed {filename} to {new_filename}')

        print("所有图片已成功重命名。")


# 使用示例
source_folder = "/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/FSGGAN/contaminate_object/img_align_rand_gt"  # 替换为你的文件夹路径
# rename_images(source_folder, 27000, 29999, 100000)
rename_gt(source_folder, 0, 286999)
