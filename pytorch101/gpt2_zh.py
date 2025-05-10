# 导入所需库
import torch
import time
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 模型文件所在路径，根据你的实际位置进行修改
model_path = "/home/pi/pytorch101/gpt-2/Wenzhong-GPT2-110M"

# 加载 GPT2 中文模型和对应的分词器（Tokenizer）
# from_pretrained 会自动从目录加载 config.json、pytorch_model.bin、tokenizer 文件等
model = GPT2LMHeadModel.from_pretrained(
    model_path,
    torch_dtype=torch.float64
)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
# 设置模型为评估模式（关闭 dropout 等训练相关功能）
model.eval()

# 打印提示语
print(">>> GPT2 中文模型，输入中文内容后回车，输入 exit 退出")
#用户名
#user_name=input("你的名字是？   ")
user_name="主人"
# 开始循环，支持多轮输入
while True:
    # 读取用户输入
    input_text = input(f"{user_name}：")
    if input_text.strip().lower() == "exit":
        break  # 输入 "exit" 时退出循环
    start=time.time()
    input_text="关于春天描写  春天来了"
    print(f"输入文本是  {input_text}")
    #提示词文本
    #promtp_text=f"提问者名字是{user_name}他们问你你要回答"
    #input_text=promtp_text+input_text

    # 使用 tokenizer 编码输入文本，返回 PyTorch Tensor 格式
    inputs = tokenizer(input_text, return_tensors="pt")
    # 关闭梯度计算，加速推理
    with torch.no_grad():
        # 使用 generate 方法生成文本
        outputs = model.generate(
            inputs["input_ids"],     # 输入编码
            attention_mask=inputs["attention_mask"],
            max_length=512,          # 生成最大长度
            do_sample=True,          # 使用采样(true)贪婪搜索(false)
            top_k=100,                # top-k 采样，文本的一致行
            top_p=1,              # nucleus 采样（top-p），文本多样行
            temperature=0.2,         # 控制生成的“温度”，越高越随机
            repetition_penalty=1.2,  #重复惩罚
            pad_token_id=tokenizer.eos_token_id  # 避免 padding 报错
        )

    generated_ids=outputs[0]
    # 解码模型输出的 token ids 为文本
    generated = tokenizer.decode(generated_ids[inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    
    #generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # 打印模型生成的结果
    print(f"GPT:{generated}\n用时{time.time()-start:.2f}s")
