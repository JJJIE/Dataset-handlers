import numpy as np
import cv2
from PIL import Image


# 获取人脸图像数据和标签
# images = data['images']
# labels = data['labels']

# img = cv2.imread('img_align_celeba/000001.jpg')

# 定义遮挡块的大小和数量
block_size = 50
num_blocks = 5

# 生成随机坐标
for i in range(1, 10001):
    filename = '{:06d}.jpg'.format(i)
    img = cv2.imread('img_align_celeba/' + filename)

   # cv2.imwrite('original/' + filename, img)
    h, w = img.shape[:2]
    x_coords = np.random.randint(0, w-block_size, num_blocks)
    y_coords = np.random.randint(0, h-block_size, num_blocks)

    # 绘制矩形并将像素设置为黑色
    for x, y in zip(x_coords, y_coords):
        cv2.rectangle(img, (x, y), (x+block_size, y+block_size), (0, 0, 0), -1)

    cv2.imwrite('masked/' + filename, img)



# cv2.imshow('masked image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 将数据集拆分为训练集和验证集
# train_images = masked_images[:10000]
# train_labels = labels[:10000]
# val_images = masked_images[10000:11000]
# val_labels = labels[10000:11000]

# 保存数据集
# np.savez("path/to/celeba/masked_celeba.npz",
        # train_images=train_images, train_labels=train_labels,
        # val_images=val_images, val_labels=val_labels)