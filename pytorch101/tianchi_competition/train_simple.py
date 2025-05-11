"""
使用 ResNet18 模型，预测宠物图像的年龄
模型来源：https://download.pytorch.org/models/resnet18-f37072fd.pth
（注：本例中我们未加载预训练权重，而是从头训练）

依赖库 pip install <以下的库>
torch
torchvision
pillow
"""

import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models #模型导入
from PIL import Image  # 图像处理库
import os



# 1. 定义自定义数据集类
class PetDataset(Dataset):  # Dataset 是 PyTorch 的数据基类
    def __init__(self, txt_path, image_folder, transform=None):
        self.image_folder = image_folder
        self.transform = transform
        with open(txt_path, 'r') as f:
            self.lines = f.readlines()  # 每一行格式为: 图片名 年龄

    def __len__(self):
        return len(self.lines)  # 数据集的大小

    def __getitem__(self, idx):
        image_name, age = self.lines[idx].strip().split()
        image_path = os.path.join(self.image_folder, image_name)
        image = Image.open(image_path).convert("RGB")  # 打开图片，并确保为 RGB 格式
        age = float(age)  # 年龄是一个浮点数（真实值回归）
        if self.transform:
            image = self.transform(image)
        return image, age  # 返回图像和年龄标签



# 2. 图像预处理和数据加载器
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 统一尺寸为224x224
    transforms.ToTensor()           # 转换为张量，数值归一化到[0,1]
])



# 加载数据集（文件路径和图像文件夹）
dataset = PetDataset('./annotations/annotations/train.txt', './trainset/trainset', transform)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)  # batch_size=16，训练时每次取16张图片，打乱顺序



# 3. 构建模型（使用 ResNet18）
model = models.resnet18(pretrained=False)  # 不加载预训练权重，从头开始训练
model.fc = nn.Linear(512, 1)  # 替换原本分类用的全连接层为回归输出（预测一个年龄值）



# 4. 定义损失函数和优化器
loss_fn = nn.MSELoss()  # 均方误差损失，用于回归问题
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)  # 使用 Adam 优化器，学习率为0.01



# 5. 开始训练
for epoch in range(5):  # 总共训练5轮，每轮遍历整个数据集一次
    total_loss = 0  # 初始化当前轮的总损失

    for images, ages in dataloader:  # 每次从 dataloader 中取一批数据
        preds = model(images).squeeze(1)  # 模型输出预测结果，squeeze(1) 把多余的维度删掉

        loss = loss_fn(preds, ages)  # 计算预测值与真实值之间的误差

        optimizer.zero_grad()  # 清除旧的梯度值
        loss.backward()        # 反向传播，计算新梯度
        optimizer.step()       # 更新参数，让模型变得更“聪明”

        total_loss += loss.item()  # 累计这批的损失

    # 每轮结束后输出损失情况，便于观察训练效果
    print(f"Epoch {epoch+1}, Loss: {total_loss:.2f}")