#!/usr/bin/env python3
from PIL import Image
import sys

def analyze_image_channels(image_path):
    try:
        # 打开图像
        with Image.open(image_path) as img:
            # 获取图像模式和通道数
            mode = img.mode
            channels = img.getbands()

            print(f"Image Mode: {mode}")
            print(f"Number of Channels: {len(channels)}")
            print("Channels:", ', '.join(channels))

            # 分别输出每个通道的信息
            for i, channel in enumerate(channels):
                channel_data = img.getchannel(channel)
                print(f"\nChannel {i+1} ({channel}) info:")
                print(channel_data)

    except IOError:
        print("Error: Cannot open the image file.")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python analyze.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    analyze_image_channels(image_path)
