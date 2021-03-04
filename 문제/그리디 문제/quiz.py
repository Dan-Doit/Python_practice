
num = input()
num_arr = []

for i in num:
    num_arr.append(int(i))

count_01 = 0
count_10 = 0

for i in range(0,len(num)-1):
    if num_arr[i] == 0 and num_arr[i+1] == 1:
        count_01 += 1
    elif num_arr[i] == 1 and num_arr[i+1] == 0:
        count_10 += 1
    else:
        continue

result = max(count_01,count_10)

print(result)