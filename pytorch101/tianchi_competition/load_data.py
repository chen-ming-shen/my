import os
from PIL import Image

# 设置数据路径（你要根据自己机器上的路径修改）
image_folder = "阿里云天池学习赛/参数项目/trainset/"
annotation_file = "阿里云天池学习赛/参数项目/annotations/annotations/train.txt"

# 读取标签文件
with open(annotation_file, 'r') as f:
    lines = f.readlines()

# 打印前5行看看长什么样
for line in lines[:5]:
    image_name, age = line.strip().split()
    image_path = os.path.join(image_folder, image_name)
    # 打开图像
    image = Image.open(image_path)
    print(f"{image_name}: {age}个月, 图像大小: {image.size}")
