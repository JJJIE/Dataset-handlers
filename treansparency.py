from PIL import Image
import os

def black_to_transparency(img):
    # 将图片转换为 RGBA（如果不是的话）
    img = img.convert("RGBA")

    # 加载图片数据
    datas = img.getdata()

    newData = []
    for item in datas:
        # 改变所有黑色（也可以是其他颜色）部分为透明
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    return img

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            img = Image.open(file_path)
            img = black_to_transparency(img)
            # 保存修改后的图片
            img.save(file_path)

# 设置包含 PNG 文件的文件夹路径
folder_path = '/home/user/generative_inpainting/test/mask_rates_30/'
process_folder(folder_path)
