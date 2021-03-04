maze = [[0 for i in range(19)] for j in range(19)]

m = int(input())
for i in range(m):
    a,b = map(int,input().split(" "))
    maze[a-1][b-1] = 1


for i in range(19):
    print(" ".join(str(i) for i in maze[i]))