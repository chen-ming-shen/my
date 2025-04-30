import torch
import numpy as np
#从数据导入张量
data=[[1,1],[1,1]]
torch_data=torch.tensor(data)
print(torch_data)
#从np数组导入张量
np_array=np.array(data)
np_torch=torch.from_numpy(np_array)
print(np_torch)
#从其他张量导入数据到新的张量
ones_data=torch.ones_like(torch_data)
rand_data=torch.rand_like(ones_data,dtype=torch.float)
print(f"一个只包含1的张量，其他元素不变：\n{ones_data}\n\n一个结构相同但是数据类型是浮点数的张量，每个数据在0-1之间随机：\n{rand_data}")
