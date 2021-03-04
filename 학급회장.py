
n = int(input())

xx = 0
arr = [[0 for j in range(5)]for i in range(3)]
arr[0][0] = 1
arr[1][0] = 2
arr[2][0] = 3

for i in range(n):
    x,y,z = map(int,input().split(" "))
    arr[0][4] += x
    arr[1][4] += y
    arr[2][4] += z
    arr[0][x] += 1
    arr[1][y] += 1
    arr[2][z] += 1

ans = arr
for n in range(4,1,-1):
    arr = sorted(ans,key=lambda x:x[n])
    xx = arr[len(arr)-1][n]
    ans = []
    for i in arr:
        if i[n] == xx:
            ans.append(i)

if len(ans)>1 :
    print("0 " + str(ans[0][4]))
else:
    print(str(ans[len(ans)-1][0]) + " " +str(ans[len(ans)-1][4]))