x = int(input())
y = 0
count = 0
up = 0
down = 0

while True:
    count += 1
    if x < count:
        break
    else:
        y += 1
        x = x - count

if x != 0:
    y += 1

if count % 2 == 1:
    up = y
    down = 1
    for i in range(x):
        if i == 0:
            continue
        else:
            up -= 1
            down += 1
else:
    up = 1
    down = y
    for i in range(x):
        if i == 0:
            continue
        else:
            up += 1
            down -= 1

print(str(up)+'/'+str(down))