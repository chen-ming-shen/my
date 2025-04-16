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
    direction=[
        [start_my[0],start_my[1]-1],
        [start_my[0],start_my[1]+1],
        [start_my[0]-1,start_my[1]],
        [start_my[0]+1,start_my[1]]
        ]#存储方向的变量
    
    while True:
        if start_my == end:
            return route
        for 
    return intersection
    pass
def bfs (maze,start,end):#广度
    pass
#输出路径怎么走和有几个走法
dfs_print=dfs(maze,start,end)
print(dfs_print)
