from PIL import Image
import random

# 加载mask图片并去除白色背景
mask_image_path = '000005.jpg'  # 替换为你mask图片的路径
mask_image = Image.open(mask_image_path).convert("RGBA")
# mask_image = mask_image.resize((256, 256))
datas = mask_image.getdata()
new_data = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
mask_image.putdata(new_data)

# 加载人脸图片
face_image_path = '27000.jpg'  # 替换为你的人脸图片路径
face_image = Image.open(face_image_path).convert("RGBA")
face_image = face_image.resize((128, 128))

# # 获取人脸图片和mask图案的尺寸
# face_width, face_height = face_image.size
# mask_width, mask_height = mask_image.size
#
# # 计算可以将mask放置的中间区域
# # 我们确保mask图案不会超出图片边缘
# x_min = (face_width - mask_width) // 2
# y_min = (face_height - mask_height) // 2
#
# # 生成mask图案在人脸图片中间区域的随机位置
# x = random.randint(x_min, x_min + mask_width)
# y = random.randint(y_min, y_min + mask_height)

# 将mask图案覆盖到人脸图片的随机位置
face_image.paste(mask_image, mask_image)

# 将最终的图像保存下来
final_image = face_image.convert("RGB")
final_image.save('path_to_save_the_result.jpg')  # 替换为你想要保存的最终图片路径
