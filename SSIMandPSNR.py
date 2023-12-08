from skimage import io
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import os


def calculate_average_ssim(folder1, folder2, num_images):
    total_ssim = 0.0

    for i in range(1, num_images + 1):
        image1_path = os.path.join(folder1, f"{i}.jpg")
        image2_path = os.path.join(folder2, f"{i}_res.jpg")

        image1 = io.imread(image1_path)
        image2 = io.imread(image2_path)

        # 确保图像尺寸一致
        if image1.shape != image2.shape or image1.shape != (256, 256, 3):
            raise ValueError(f"Image size mismatch or not 256x256x3 at index {i}")

        ssim_value = ssim(image1, image2, channel_axis=-1)
        total_ssim += ssim_value

    return total_ssim / num_images

def calculate_average_psnr(folder1, folder2, num_images):
    total_psnr = 0.0

    for i in range(1, num_images + 1):
        image1_path = os.path.join(folder1, f"{i}.jpg")
        image2_path = os.path.join(folder2, f"{i}_res.jpg")

        image1 = io.imread(image1_path)
        image2 = io.imread(image2_path)

        psnr_value = psnr(image1, image2)
        total_psnr += psnr_value

    return total_psnr / num_images


# 设置文件夹路径和图像数量
folder1 = '/home/user/GLCIC-PyTorch/test/hq256/'
folder2 = '/home/user/GLCIC-PyTorch/results/'
num_images = 510

# 计算平均SSIM值
average_ssim = calculate_average_ssim(folder1, folder2, num_images)
print(f"Average SSIM: {average_ssim}")
average_psnr = calculate_average_psnr(folder1, folder2, num_images)
print(f"Average PSNR: {average_psnr}")
