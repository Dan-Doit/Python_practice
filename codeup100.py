
maze = []
for i in range(10):
    maze.append(input().split(" "))
#     R,D
nx = [1,0]
ny = [0,1]
x, y = 1, 1
while True:
    if maze[y+1][x] =='1' and maze[y][x+1]=='1':
        maze[y][x] = 9
        break
    if maze[y][x]=='2':
        maze[y][x]=9
        break
    # 현재값 9로 만들기
    maze[y][x] = 9


    if maze[y][x+1] == '1':
        x += nx[1]
        y += ny[1]
    else:
        x += nx[0]
        y += ny[0]


for i in maze:
    print(" ".join(str(j) for j in i))
