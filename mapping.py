import os


def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    return sorted(
        [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(tuple(image_extensions))],
        key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))


def create_mapping_file(root_folder, output_file):
    train_folder = os.path.join(root_folder, 'train')
    categories = sorted(os.listdir(train_folder))

    all_image_paths = []
    for category in categories:
        category_folder = os.path.join(train_folder, category)
        image_paths = get_image_paths(category_folder)
        all_image_paths.extend(image_paths)

    sorted_image_paths = sorted(all_image_paths, key=lambda x: int(os.path.splitext(os.path.basename(x.split('/')[-1]))[0]))

    with open(output_file, 'w') as f:
        for image_path in sorted_image_paths:
            f.write(image_path + '\n')


if __name__ == "__main__":
    root_folder = 'IMG'  # 希望创建mapping的文件夹路径
    output_file = os.path.join(root_folder, 'mapping.txt')

    create_mapping_file(root_folder, output_file)
    print(f"mapping.txt 文件已生成在 {output_file}")
