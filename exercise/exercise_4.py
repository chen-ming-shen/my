#sorted()使用
#假设我们用一组tuple表示学生的名字和成绩
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    #按名字排序
    t=str.lower(t[0])
    return t
def by_score(t):
    #按成绩高低排序
    t=abs(t[1])
    return t
L2=sorted(L,key=by_name)
print(f'按名字排序:\n{L2}\n')
print(f'成绩高到低排序:\n{sorted(L,key=by_score)}')

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter(times=0):
    def counter():
        nonlocal times
        times=times+1
        return times
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#请用匿名函数改造以下面的代码;
def is_odd(n):
    return n%2==1
L=list(filter(lambda n: n%2==1,range(1,20)))
print(L)
