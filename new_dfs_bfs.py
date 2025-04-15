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
    start=list(start)
    end=list(end)
    
    route=[]#这个是记录路径的
    start_my=start#使用一个变量保存动态的位置
    intersection=[]#记录遇到的路口
    
    while True:
        intersection=[]
        for maze_y in maze[start_my[0]]:
            for maze_x in maze_y[start_my[1]]:
                route.append(maze_y)#记一个点
        #存储方向的变量
        direction=[
        [start_my[0],start_my[1]-1],
        [start_my[0],start_my[1]+1],
        [start_my[0]-1,start_my[1]],
        [start_my[0]+1,start_my[1]]
        ]
        for start_my_tmp in direction
            if start_my_tmp[0] <= 0:
                if start_my_tmp[1] <=0:
                    intersection.append(start_my_tmp)
                    #记录当前位置遇到的路口，如果没有路口则记录的是下一步的位置
    pass
def bfs (maze,start,end):#广度
    pass
#输出路径怎么走和有几个走法