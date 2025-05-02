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
