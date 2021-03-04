
test = int(input())
#  파이썬은 재귀가 1000이상 넘어가면 오류를 발생하는데
#  이코드를 사용하면 재귀를 늘릴수있다.
import sys
sys.setrecursionlimit(10 ** 4)


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        # 여기서 배열을 부르면 어떤 배열을 다시 찾으라고하는지 모름
        # 그렇기때문에 DFS인지 배열인지 확인하자
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False

for _ in range(test):
    n,m,k = map(int,input().split(" "))
    arr = []
    arr = [[0 for _ in range(m)]for _ in range(n)]


    for i in range(k):
        x,y = map(int,input().split(" "))
        arr[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if DFS(i, j) == True:
                result += 1

    print(result)



