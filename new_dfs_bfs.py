maze=[
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
    ]
start=(0,0)
end=(4,4)
def dfs (maze,start,end):#深度
    #走这个行为的实现要在一个 while 里实现
    tmp=["路径"]#用来调试用的
    route=[list(start)]#这个是记录路径的，先加了起始坐标
    start_my=list(start)#使用一个变量保存动态的位置
    intersection=[]#记录遇到的路口
    while True:
        if start_my == list(end):
            return route #如果循环的坐标对象等于终点坐标时返回所有路径
        intersection_tmp=[]
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:#dx and dy 是xy的变化量
            x,y = start_my
            nx,ny =x+dx,y+dy
            if 0<= nx< len(maze) and  0<= ny < len(maze[0]):#选择除墙壁外的位置
                if maze[nx][ny]==0:
                    intersection_tmp.append([nx,ny])#如果是可以走的路添加到临时变量里
        start_my=[intersection_tmp[0][0],intersection_tmp[0][1]]#更新位置变量
        route.append(start_my)
        tmp.append(route)
    return tmp
def bfs (maze,start,end):#广度
    pass
#输出路径怎么走和有几个走法
dfs_print=dfs(maze,start,end)
print(dfs_print)
