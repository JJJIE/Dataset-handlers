from PIL import Image


def extract_channels(input_path):
    # 打开图片
    image = Image.open(input_path)

    # 确保图片是RGB模式
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # 分离RGB三个通道
    r, g, b = image.split()

    # 为了可视化方便，我们为每个通道创建一个全新的彩色图像，并设置其他两个通道为0
    r_img = Image.merge('RGB', (r, Image.new("L", r.size), Image.new("L", r.size)))
    g_img = Image.merge('RGB', (Image.new("L", r.size), g, Image.new("L", r.size)))
    b_img = Image.merge('RGB', (Image.new("L", r.size), Image.new("L", r.size), b))

    # 保存三个通道为单独的图片
    r_img.save('r_channel.jpg')
    g_img.save('g_channel.jpg')
    b_img.save('b_channel.jpg')


# 调用函数并传入你的png图片路径
extract_channels('/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/CelebAMask-HQ/CelebA-HQ-img/111.jpg')
