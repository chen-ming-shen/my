
"""
maze = [
  [0, 0, 1, 0],
  [1, 0, 1, 0],
  [1, 0, 0, 0],
  [1, 1, 1, 0]
]
origin=(0,0)#开始
end=(len (maze[0]),len(maze))#结束
current_location=list(origin)#当前位置里加入起点
inspect=set()#用来检查走过的地方
use_stack=[[0,0],[0,0]]#用来模拟栈的列表
intersection=[]#记录路口
while True:
    if use_stack:
        if use_stack[-1]==end:#如果当前位置是终点时
            print (length)#路径长度
            print (route)#路径
    x,y=use_stack.pop()
    for nx ,ny in [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]:
        if 0<= nx <= end[0] and 0<= ny <= end[1] and (nx,ny ) not in inspect:
            ins_x=maze[ny]
            if ins_x[nx]==0:
                current_location=nx,ny
                inspect.add(tuple([nx,ny]))
                intersection.append([nx,ny])
                use_stack.append([nx,ny])
            else:
                break
        else:
            break
print(use_stack)
"""

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
#elif trim('  hello  world  ') != 'hello  world':
    #print(trim('  hello  world  '))
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('所有测试成功!')
