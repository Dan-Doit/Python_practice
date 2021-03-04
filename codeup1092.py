# student = [0]*24
# n = int(input())
# call = list(map(int,input().split(' ')))
# for i in call:
#     student[i] = student[i] + 1
#
# for i in range(1,24):
#     print(student[i],end=' ')

a = input()
b = input().split()

n = list(map(int,b))
arr = []

for i in range(24):
    arr.append(0)

for i in n:
    arr[i] = arr[i] + 1

for i in range(1, 24):
    print(arr[i],end=' ')


