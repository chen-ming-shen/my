maze=[
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
    ]
start=(1,3)
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
def dfs_choice (maze,start,end):
    #方向
    #上(-1,0),下(+1,0),左(0,-1),右(0,+1)
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
    需要维护的变量：
    存储当前位置的一个
    存储方向选择的列表
    存储路径的列表
    '''
    #方向列表
    direction=[
        [-1,0],
        [1,0],
        [0,-1],
        [0,1]
        ]#上(-1,0),下(+1,0),左(0,-1),右(0,+1)
    cl_my=[]#我的当前位置
    route=[]#路
    coord=[]#坐标上的数值 在有墙壁地图里的位置
    end=list(end)
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
    
def coord_f_b_l_r (maze,dfs_choice):
    coord_obj=[]
    cl_my=[]
    cl_my.append(dfs_choice[1])
    dfs_choice_coord=dfs_choice[0]
    coord_obj.append(dfs_choice_coord[0])
    #cl_my是当前的位置，coord_obj是当前位置的值
    #求出当前位置四周的值判断接下来前进的方向
    front=[]
    back=[]
    left=[]
    right=[]
    now=cl_my[0]
    
    front_tmp=now[0]
    front_tmp -= 1
    front=[front_tmp]
    front.append(now[1])
    
    back_tmp=now[0]
    back_tmp += 1 
    back=[back_tmp]
    back.append(now[1])
    
    left_tmp=now[1]
    left_tmp -= 1
    left=[left_tmp]
    left.insert(0,now[0])
    
    right_tmp=now[1]
    right_tmp += 1
    right=[right_tmp]
    right.insert(0,now[0])
    
    now_tmp=[front]+[back]+[left]+[right]

    coord=[]
    for tmp_of_now in now_tmp:
        now_tmp_Y = tmp_of_now[1]
        now_tmp_X = tmp_of_now[0]
        maze_tmp=maze[now_tmp_X]
        coord_tmp=maze_tmp[now_tmp_Y]
        coord.append(coord_tmp)
    return coord
def dfs (coord,maze,choice):#深度优先搜索
    pass
def bfs (maze,start,end):#广度优先搜索
    pass
maze=main_line()
dfs_choice=dfs_choice(maze,start,end)
coord_f_b_l_r=coord_f_b_l_r(maze,dfs_choice)

print(maze)
print(dfs_choice)
print(coord_f_b_l_r)

print(dfs(maze,start,end))
print(bfs(maze,start,end))
