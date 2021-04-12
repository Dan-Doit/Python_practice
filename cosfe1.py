
import re

ans = ["",""]
times = []
for _ in range(int(input())):
    times.append(re.split(' ~ |:',input()))

for i in range(len(times)):
    front1 = ''
    back1 = ''
    for t in range(len(times[i])):
        if t < 2 :
            front1 += times[i][t]
        else:
            back1 += times[i][t]

    front2 = ''
    back2 = ''
    for t in range(len(times[i+1])):
        if t < 2 :
            front1 += times[i][t]
        else:
            back1 += times[i][t]

    if int(front1) < int(front2):
        ans[0] = front1