
n = int(input())
arr = [[0 for col in range(n)]for raw in range(n)]
half = int((n/2))
for i in range(n):
    for j in range(n):
        arr[0][j] = 1
        arr[i][0] = 1
        arr[n-1][j] = 1
        arr[i][n-1] = 1
        arr[half][half] = 8
        print(arr[i][j],end=' ')
    print()