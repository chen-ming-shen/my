import json
from collections import defaultdict
import random

class 语言学习模型:
    def __init__(self, 记忆文件='A记忆.json'):
        self.属性文本库 = defaultdict(list)
        self.文本属性库 = defaultdict(set)
        self.记忆文件 = 记忆文件
        self.加载记忆()
        self.上一个输出 = None
        self.对话历史 = []  # 添加历史记录列表

    def 加载记忆(self):
        """从外部文件加载文本属性库"""
        try:
            with open(self.记忆文件, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.属性文本库 = defaultdict(list, {k: v for k, v in data['属性文本库'].items()})
                self.文本属性库 = defaultdict(set, {k: set(v) for k, v in data['文本属性库'].items()})
            print("记忆加载成功！")
        except FileNotFoundError:
            print("未找到记忆文件，模型将在对话中学习新的内容。")

    def 保存记忆(self):
        """将文本属性库保存到外部文件"""
        with open(self.记忆文件, 'w', encoding='utf-8') as file:
            json.dump({
                '属性文本库': dict(self.属性文本库),
                '文本属性库': {k: list(v) for k, v in self.文本属性库.items()}
            }, file, ensure_ascii=False, indent=4)
        print(f"记忆已保存至 {self.记忆文件}")

    def 添加关联(self, 文本, 属性):
        """将属性与文本进行关联"""
        if 属性 not in self.文本属性库[文本]:
            self.属性文本库[属性].append(文本)
            self.文本属性库[文本].add(属性)
            print(f"已学习: '{文本}' 关联 '{属性}'")
        else:
            print(f"'{文本}' 已经关联了属性 '{属性}'，请添加不同的属性。")

    def 推理输出(self, 输入文本):
        """根据输入文本进行推理输出"""
        输入文本列表 = list(输入文本)
        输出文本集合 = set()
        属性集合 = set()

        for i in range(len(输入文本列表)):
            for j in range(i + 1, len(输入文本列表) + 1):
                当前文本 = ''.join(输入文本列表[i:j])
                if 当前文本 in self.文本属性库:
                    当前属性集合 = self.文本属性库[当前文本]
                    属性集合.update(当前属性集合)

        if 属性集合:
            输出文本 = random.choice(list(属性集合))  # 随机选择一个属性输出
            if self.上一个输出 == 输出文本:
                print(f"重复输出，重新推理...")
                self.推理输出(输入文本)
            else:
                print(f"模型输出：{输出文本}")
                self.上一个输出 = 输出文本
                self.记忆推理结果(输出文本)
        else:
            print(f"输入的文本 '{输入文本}' 不在记忆中，无法推理。")

    def 记忆推理结果(self, 输出文本):
        """将推理结果进行记忆"""
        for 文本 in 输出文本.split(', '):
            文本 = 文本.strip()
            if 文本 not in self.文本属性库:
                print(f"记忆推理结果: '{文本}'")
                属性 = input(f"请输入 '{文本}' 的属性: ")
                self.添加关联(文本, 属性)

    def 查看记忆(self):
        """查看当前记忆内容"""
        print("\n当前记忆内容：")
        print("属性与文本的关联:")
        for 属性, 文本列表 in self.属性文本库.items():
            print(f"  '{属性}': {', '.join(文本列表)}")
        print("\n文本与属性的关联:")
        for 文本, 属性集合 in self.文本属性库.items():
            print(f"  '{文本}': {', '.join(属性集合)}")

    def 更改记忆(self):
        """更改记忆中的内容"""
        文本 = input("请输入要更改的文本: ")
        if 文本 in self.文本属性库:
            属性集合 = self.文本属性库[文本]
            print(f"当前属性: {', '.join(属性集合)}")
            新属性 = input("请输入新的属性: ")
            self.文本属性库[文本] = {新属性}
            for 属性 in 属性集合:
                self.属性文本库[属性] = [t for t in self.属性文本库[属性] if t != 文本]
            self.添加关联(文本, 新属性)
            print(f"已更改: '{文本}' 的属性为 '{新属性}'")
        else:
            print(f"文本 '{文本}' 不在记忆中。")

    def 清空记忆(self):
        """清空所有记忆"""
        self.属性文本库.clear()
        self.文本属性库.clear()
        print("所有记忆已清空。")

    def 对话学习(self):
        """通过对话形式学习新属性和文本"""
        print("开始对话（输入'退出'结束对话，输入'查看'查看当前记忆，输入'更改'更改记忆，输入'清空'清空所有记忆）:")
        while True:
            输入文本 = input("你: ")
            self.对话历史.append(输入文本)  # 记录对话历史
            if 输入文本 == "退出":
                print("对话结束。")
                self.保存记忆()
                break
            elif 输入文本 == "查看":
                self.查看记忆()
            elif 输入文本 == "更改":
                self.更改记忆()
            elif 输入文本 == "清空":
                self.清空记忆()
            elif "(" in 输入文本 and ")" in 输入文本:
                文本, 属性 = 输入文本.split("(")[0].strip(), 输入文本.split("(")[1].rstrip(")").strip()
                self.添加关联(文本, 属性)
            else:
                self.推理输出(输入文本.strip())

if __name__ == "__main__":
    model = 语言学习模型()
    model.对话学习()