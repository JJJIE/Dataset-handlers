import os


def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(tuple(image_extensions))]


# def create_mapping_file(root_folder, output_file):
#     train_folder = os.path.join(root_folder)
#     categories = sorted([f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))])
#
#     all_image_paths = []
#     for category in categories:
#         category_folder = os.path.join(train_folder, category)
#         image_paths = get_image_paths(category_folder)
#         all_image_paths.extend(image_paths)
#
#     sorted_image_paths = sorted(all_image_paths)  # 直接对文件名进行排序
#
#     with open(output_file, 'w') as f:
#         for image_path in sorted_image_paths:
#             f.write(image_path + '\n')


def create_mapping_file(folder_path, output_file):   # 没有子文件夹
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    all_image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(tuple(image_extensions))]
    sorted_image_paths = sorted(all_image_paths)

    with open(output_file, 'w') as f:
        for image_path in sorted_image_paths:
            f.write(image_path + '\n')


if __name__ == "__main__":
    root_folder = '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_celeba_hq'  # 希望创建mapping的文件夹路径
    output_file = os.path.join('celeba_hq_mapping.txt')

    create_mapping_file(root_folder, output_file)
    print(f"mapping.txt 文件已生成在 {output_file}")
