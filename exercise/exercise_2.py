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
