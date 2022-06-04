index = int(input())

x, y = 0, index-1

array = [[' ' for i in range(index)] for i in range(index)]

for i in range(index):
    for j in range(index):
        if i == 0 or i == index - 1:
            array[i][j] = '*'
        if j == 0 or j == index - 1:
            array[i][j] = '*'
        if j == x or j == y:
            array[i][x] = '*'
            array[i][y] = '*'
    x = x + 1
    y = y - 1
    print(''.join(array[i]))