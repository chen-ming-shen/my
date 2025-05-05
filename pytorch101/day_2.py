import torch
'''
#练习pytorch
#张量类似py的列表结构
#张量的运算
x=torch.tensor([1.0,2.0])
y=torch.tensor([3.0,4.0])
#元素级运算
z=x+y
z=x*y#逐元素乘法
print(z)
#矩阵乘法
mat1=torch.rand(2,3)
mat2=torch.rand(3,4)
mat3=mat1@mat2
print(mat3)

#（疑问）为什么矩阵乘法结果是2×4的矩阵

t=torch.arange(0,12)#创建1D的向量
print(t)
t=t.view(3,4)#改成3×4的矩阵
print(t)
t=t.reshape(2,6)#重新形状
print(t)
t=t.unsqueeze(0)#添加一个新维度
print(t)
t=t.squeeze()#移除维度为1的维度
print(t)
'''
print(torch.rand(1,3,1,5))
#.shape长度 .dim()几维