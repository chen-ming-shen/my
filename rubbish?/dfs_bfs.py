maze=[
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
    ]
start=(0,0)
end=(4,4)
def main_line ():
    global maze
    for maze_line in maze:
        maze_line.append(1)
        maze_line_end=[]
        maze_line_end.append(maze_line)
    maze_line=[]
    length=len(maze_line)
    one_line=[]
    for maze_line_end_one in maze_line_end:
        maze_line_end_times=len(maze_line_end_one)
    maze_line_end_times-=1
    for one in range(maze_line_end_times):
        one=[]
        one_line.append(1)
    maze.insert(0,one_line)
    maze.append(one_line)
    for maze_end_two in maze:
        maze_end_two.insert(0,1)
        maze_end_two_to=[]
        maze_end_two_to.append(maze_end_two)
        maze_end_two=[]
    return maze
def dfs_choice (maze1,start,end):
    '''
    maze=[
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
    ]
    '''
    #方向列表
    direction=[
        [-1,0],
        [1,0],
        [0,-1],
        [0,1]
        ]
    cl_my=[]#我的当前位置
    route=[]#路
    coord=[]#坐标上的数值 在有墙壁地图里的位置
    #end=list(end)
    start_tmp_one=[]
    for start_tmp in start:
        start_tmp+=1
        start_tmp_one.append(start_tmp)
    cl_my=start_tmp_one
    cl_my_0=cl_my[0]
    cl_my_1=cl_my[1]
    maze_tmp=maze[cl_my_0]
    coord_obj_int=(maze_tmp[cl_my_1])
    coord_obj=[]
    coord_obj.append(coord_obj_int)
    coord_obj.append(0)
    coord=[]
    coord.append(coord_obj)#在地图里位置的值
    coord.append(cl_my)#当前我的位置
    return coord
    #dfs_choice是当前的位置和当前位置的值  
def coord_f_b_l_r (maze1,dfs_choice):
    #求出当前位置四周的值判断接下来前进的方向
    front=[]
    back=[]
    left=[]
    right=[]
    now=dfs_choice[1]
    coord=[]

    now_tmp=[
      [now[0]-1,now[1],],
      [now[0]+1,now[1],],
      [now[0], now[1]-1],
      [now[0], now[1]+1]
      ]
    coord_1=[]
    for tmp_of_now in now_tmp:
        now_tmp_Y = tmp_of_now[1]
        now_tmp_X = tmp_of_now[0]
        maze_tmp=maze[now_tmp_X]
        coord_tmp=maze_tmp[now_tmp_Y]
        coord_1.append(coord_tmp)
    coord.append(now_tmp)
    coord.append(coord_1)
    return coord
    
def dfs (maze1,dfs_choice,coord_f_b_l_r):#深度优先搜索
    '''
    接受的一个地图带墙壁的 maze
    一个位置和值 dfs_choice
    一组前后左右位置和对应的值 coord_f_b_l_r
    存储路径的列表 route
    '''
    global start
    route=[list(start)]
    tmp=0
    coord_one=coord_f_b_l_r[1]
    coord_two=coord_f_b_l_r[0]
    for coord_one_tmp in coord_one:
        if coord_one_tmp == 0:
            route.append(coord_two[tmp])
            tmp += 1
        else:
            tmp += 1
    route_len=len(route)
    route_len -= 1
    start=route[route_len]
    return start
def bfs (maze,start,end):
    pass
'''
maze=main_line()
dfs_choice=dfs_choice(maze,start,end)
coord_f_b_l_r=coord_f_b_l_r(maze,dfs_choice)
dfs=dfs(maze,dfs_choice,coord_f_b_l_r)

print(maze)
print(dfs_choice)
print(coord_f_b_l_r)
print(dfs)
end=[end]
'''
bug=20
maze=main_line()
# 原始坐标 → 扩展后坐标
adjusted_start = (start[0] + 1, start[1] + 1)
adjusted_end = (end[0] + 1, end[1] + 1)
while True:
    if bug == 0:
            print(bug)
            break
    else:
        if dfs == adjusted_end:
            print(dfs_res)
        else:
            choice=dfs_choice(maze,start,end)
            coord=coord_f_b_l_r(maze,choice)
            dfs_res=dfs(maze,choice,coord)
            
            print(choice)
            print(coord)
            print(dfs_res)
            bug -= 1
print(bfs(maze,start,end))
