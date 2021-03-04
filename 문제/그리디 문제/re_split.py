
# letters = str(input())
#
# nums = str([0,1,2,3,4,5,6,7,8,9])
# x = ""
# y = ""
# for i in range(1,len(letters)):
#     if letters[i] in nums:
#         x += letters[i]
#     else:
#         break
#
# for i in range(len(x)+2,len(letters)):
#     if letters[i] in nums:
#         y += letters[i]
#     else:
#         break
#
# x = int(x)
# y = int(y)
# print((x*12) + y)

import re
letters = input()
letters = re.split("C|H",letters)
letters[1] = int(letters[1])
letters[2] = int(letters[2])

print((letters[1]*12) + letters[2])