import numpy as np
import cv2
from PIL import Image


# 获取人脸图像数据和标签
# images = data['images']
# labels = data['labels']

# img = cv2.imread('img_align_celeba/000001.jpg')

# 定义遮挡块的大小和数量
block_size = 250
num_blocks = 5


# 生成随机坐标
for i in range(30000):
    # filename = '{:05d}.jpg'.format(i)
    filename = str(i) + '.jpg'
    img = cv2.imread('/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_celeba_hq/' + filename)
    # print(img)
    # img = cv2.imread('000192.jpg')

    # cv2.imwrite('original/' + filename, img)
    h, w = img.shape[:2]
    x_coords = np.random.randint(0, w-block_size, num_blocks)
    y_coords = np.random.randint(0, h-block_size, num_blocks)

    # 绘制矩形并将像素设置为黑色
    for x, y in zip(x_coords, y_coords):
        cv2.rectangle(img, (x, y), (x+block_size, y+block_size), (0, 0, 0), -1)

    # 要先创建img_celeba_hq_mask这个文件
    cv2.imwrite('/media/user/2634e654-9e1a-49b2-a9d8-fb746a23d9fd/img_celeba_hq_mask/' + filename,img)


