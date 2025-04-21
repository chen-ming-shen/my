import math




# 给定振动传感器数据：vibration = [2.1, 3.0, None, 2.8, 3.2, None, 2.9]
# 要求：1. 删除None值 2. 计算有效数据的平均值
vibration = [2.1, 3.0, None, 2.8, 3.2, None, 2.9]
# 你的代码写在这里
vibration_tmp=[v_tmp for v_tmp in vibration if v_tmp is not None]
print(sum(vibration_tmp)/len(vibration_tmp),vibration_tmp)

# 编写一个函数，输入转速(rpm)，返回角速度(rad/s)
# 公式：
def rpm_to_rads(rpm=None):
    # 你的代码写在这里
    try:
        if rpm==None:
            rpm=114
            print(rpm * 0.10472,"默认rpm=",rpm)
        else:
            rpm=float(input("输入转速(rpm)"))
            print(rpm * 0.10472)
    except Exception as e:
        print("输入了无效转速",e)
rpm_to_rads()

    #给定温度序列，连续3次超过阈值则触发报警
temps = [68, 72, 85, 87, 84, 70, 86, 88, 90]
threshold = 85
def check_alert(temps, threshold):
    # 你的代码写在这里
    third=[]
    Record=0
    for alarm_tmp in temps:
        if Record==3:
            break
        if alarm_tmp >threshold:
            third.append(alarm_tmp)
            Record+=1
        else:
            Record=0
            third=[]
    print(f"警报{third}有{Record}次连续超过阈值")
check_alert(temps, threshold)

#2025/4/20
s1 = 72
s2 = 85
r = s2 / s1-1
print(f'小明提供了{r:.2f}%')

#请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[-1][-1])

print("")
"""
练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
"""
height = 1.75
weight = 80.5

bmi = weight/(height**2)
def bmi_tmp(bmi,consequence):
    print (f"小明的BMI指数是{bmi:.2f}，结果是{consequence}")
if bmi<18.5 :
    consequence="低于18.5：过轻"
    bmi_tmp(bmi,consequence)
elif 18.5 <bmi<=25:
    consequence="18.5-25：正常"
    bmi_tmp(bmi,consequence)
elif 25 <bmi<=28:
    consequence="25-28：过重"
    bmi_tmp(bmi,consequence)
elif 28 <bmi<=32:
    consequence="28-32：肥胖"
    bmi_tmp(bmi,consequence)
elif 32<bmi:
    consequence="高于32：严重肥胖"
    bmi_tmp(bmi,consequence)
else:
    print("错误")
    
#练习
#请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print(f"hello,{l}!")

#练习
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 
#a*x**2+b*x+c 的两个解
def quadratic(a, b, c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    x=[x1,x2]
    return x
x=quadratic(1,3,1)
print(f"x的两个值是{x[0]:.2f}和{x[1]:.2f}")

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(a,*numbers):
    s=a
    for tmp in numbers:
        s=s*tmp
    return s
# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
### **汉诺塔问题描述**
#- 有三根柱子，编号为 **A、B、C**。
#- 初始时，在柱子 **A** 上有 **n 个大小不同的盘子**，盘子从上到下按 **从小到大** 的顺序叠放。
#- 目标：把所有盘子从柱子 **A** 移动到柱子 **C**，并遵守以下规则：
#  1. **每次只能移动一个盘子**。
#  2. **移动时，大盘子不能放在小盘子上**。
#  3. **可以利用柱子 B 作为辅助**。
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c,)
    a_int=[a_tmp for a_tmp in range(n)]
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(1, 'A', 'B', 'C')
