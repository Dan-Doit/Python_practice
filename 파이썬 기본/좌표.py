
# L : 왼쪽으로 한칸이동
# R : 오른쪽으로 한칸이동
# U : 위쪽으로 한칸이동
# D : 아래쪽으로 한칸이동



arr = [[[raw,col] for col in range(1,6)]for raw in range(1,6)]

dir = list(map(str,input().split('')))

x,y = 1,1

for i in range(5):
    print(arr[i])

#     L R U  D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']


for i in range(len(dir)):
    for j in range(move_type):
        if dir == move_type:
            nx = x + dx[j]
            ny = y + dy[j]

print(nx,ny)



