import os
from PIL import Image

def merge_images(jpg_path, png_path, save_path):
    # 打开JPG和PNG图像
    jpg_image = Image.open(jpg_path).convert("RGBA")
    png_image = Image.open(png_path)

    # 确保PNG图像是RGBA模式
    if png_image.mode != 'RGBA':
        png_image = png_image.convert('RGBA')

    # 确保两个图像尺寸相同
    if jpg_image.size != png_image.size:
        png_image = png_image.resize(jpg_image.size, Image.ANTIALIAS)

    # 提取PNG图像的Alpha通道
    r, g, b, a = png_image.split()

    # 合并JPG图像和PNG的Alpha通道
    merged_image = Image.merge('RGBA', (jpg_image.split()[0], jpg_image.split()[1], jpg_image.split()[2], a))

    # 保存合并后的图像
    merged_image.save(save_path, 'PNG')


def main(jpg_dir, png_dir, save_dir):
    # 创建保存目录
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 遍历JPG图像
    for jpg_file in os.listdir(jpg_dir):
        if jpg_file.endswith('.jpg'):
            # 构建文件路径
            jpg_path = os.path.join(jpg_dir, jpg_file)
            png_path = os.path.join(png_dir, os.path.splitext(jpg_file)[0] + '.png')
            save_path = os.path.join(save_dir, jpg_file)

            # 合并图像
            merge_images(jpg_path, png_path, save_path)
            print(f"Processed {jpg_file}")

if __name__ == '__main__':
    main('/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_celeba_hq',
         '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_seg',
         '/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/MR-GAN-DATA')

