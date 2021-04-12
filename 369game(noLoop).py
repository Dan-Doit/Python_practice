
def func(count,num):
    ans = 0
    if count > len(num)-1:
        return ans
    if num[count] == '3':
        ans = 1
    elif num[count] == '6':
        ans = 1
    elif num[count] == '9':
        ans = 1
    count += 1
    return ans + func(count,num)

print(func(0,'12661123334'))