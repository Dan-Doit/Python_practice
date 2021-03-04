
import string
from collections import deque


arr = []
arr.append(" ")
letters = input()
ans = []
char = []
for i in string.ascii_lowercase:
    char.append(i)
for i in string.digits:
    char.append(i)
char.append("_")
char.append("-")
char.append(".")


count = 0
for i in letters:
    if(count==15):
        break
    if i in char:
        arr.append(i)
    count += 1

for i in range(len(arr)-1,1,-1):
    if(arr[i] == "." and arr[i-1] == "."):
        arr.pop(i)

que = deque(arr)
que.popleft()

if(len(que)!=0):
    if que[len(que)-1] == "." and len(que)!=0:
        que.pop()
    if que[0] == "." and len(que)!=0:
        que.popleft()

if(len(que)==0):
    que.append("a")

while(len(que)<3):
    que.append(que[len(que)-1])

print("".join(str(i) for i in que))
