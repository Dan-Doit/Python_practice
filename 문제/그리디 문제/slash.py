index, num = list(map(int, input().split(' ')))

x = num - 1

arr = [['*' if j == 0 or j == index - 1 or i == 0 or i == index - 1 else ' ' for j in range(index)] for i in range(index)]

while x < index * 2:
    current = x
    for i in range(index):
        for j in range(index):
            if j == current:
                arr[i][j] = '*'
        current -= 1
    x = x + num

for i in arr:
    print(''.join(i))
