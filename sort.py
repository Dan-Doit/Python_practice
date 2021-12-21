index = int(input())
arr = []

for i in range(index):
    arr.append(int(input()))

newArr = list(set(arr))

for i in sorted(newArr):
    print(i)
