maze=[
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
    ]
start=(0,0)
end=(4,4)
def dfs (maze,start,end):#深度 #走这个行为的实现要在一个 while 里实现
    route=[list(start)]#这个是记录路径的，先加了起始坐标
    start_my=list(start)#使用一个变量保存动态的位置
    visited=set()#访问过的位置
    while True:
        if start_my == list(end):
            tmp=["一个路径是",route,visited]
            return tmp#如果循环的坐标对象等于终点坐标时返回数据
        visited.add(tuple(start_my))
        intersection_tmp=[]
        x,y = start_my
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:#dx and dy 是xy的变化量
            nx,ny =x+dx,y+dy
            if 0<= nx< len(maze) and  0<= ny < len(maze[0]):#选择除墙壁外的位置
                if maze[nx][ny]==0 and (nx,ny) not in visited:
                    intersection_tmp.append([nx,ny])#如果是可以走的路添加到临时变量里
        if intersection_tmp:
            start_my=intersection_tmp[0]#更新位置变量
            route.append(start_my)
        else:
            break
def bfs (maze,start,end):#广度
    pass
#输出路径怎么走和有几个走法
dfs_print=dfs(maze,start,end)
print(dfs_print)
