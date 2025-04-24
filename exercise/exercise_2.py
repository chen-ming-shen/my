import time 
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
    temporary=[]
    final=""
    for s_tmp in s :
        if s_tmp != " ":
            temporary.append(s_tmp)
    if temporary!="":
         for temporary_tmp in temporary:
            final =final+temporary_tmp
    if len (final) >=9:
         final_tmp = final[0:5]+"  "
         final_tmp =final_tmp+final[5:-1]+final[-1]
         return final_tmp
    else:
         return final
         
# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('所有测试成功!')
    
print(trim('  hello  world  '))
    
    
#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
### **汉诺塔问题描述**
#- 有三根柱子，编号为 **A、B、C**。
#- 初始时，在柱子 **A** 上有 **n 个大小不同的盘子**，盘子从上到下按 **从小到大** 的顺序叠放。
#- 目标：把所有盘子从柱子 **A** 移动到柱子 **C**，并遵守以下规则：
#  1. **每次只能移动一个盘子**。
#  2. **移动时，大盘子不能放在小盘子上**。
#  3. **可以利用柱子 B 作为辅助**。


move_times=0
n=3
def move(n, a, b, c):
    global move_times
    move_times+=1
    if n == 1:#当递归到的最底层时
        #print(f"{a} --> {c}")#对象移动到目标位置
        pass
    else:
        move(n-1,a,c,b)#依次把a移动到b里
        #print(f"{a} --> {c}")#把a移动到c里
        move(n-1,b,a,c)#然后打印出把所有盘子从b借助a移动到C的方法里
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
start_time=time.perf_counter()
move(n, 'A', 'B', 'C')
end_time=time.perf_counter()

print(f"当n={n}时，递归次数{move_times}次，也是移动步数{move_times}次\n用时{end_time - start_time:.10f}秒")





#构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
print([tmp for tmp in range(1,100,2)])




#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    min_l,max_l=None,None
    if not L:
        return (min_l,max_l)
    else:
        min_l,max_l=L[0],L[0]
        for tmp in L:
            if tmp<=min_l:
                min_l=tmp
            if tmp >= max_l:
                max_l=tmp
        return (min_l,max_l)
# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!',findMinAndMax([7]))
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!',findMinAndMax([7, 1]))
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!',findMinAndMax([7, 1, 3, 9, 5]))
else:
    print('全部测试成功!')
    
    
    
x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))
#修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [tmp.lower()  for tmp in L1 if isinstance(tmp ,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
