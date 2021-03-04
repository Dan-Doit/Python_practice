
n = int(input())
poker = []
s = []
h = []
c = []
d = []
for i in range(n):
    poker = input().split(' ')
    if poker[0] == "스페이드":
        s.append([poker[0],int(poker[1])])

    if poker[0] == "하트":
        h.append([poker[0],int(poker[1])])

    if poker[0] == "클로버":
        c.append([poker[0],int(poker[1])])

    if poker[0] == "다이아":
        d.append([poker[0],int(poker[1])])

while(True):
    if len(s) != 0:
        s.sort(key=lambda x:[1])
        print(s[0][0],s[-1][1])
        break
    elif len(h) != 0:
        h.sort(key=lambda x:[1])
        print(h[0][0], h[-1][1])
        break
    elif len(c) != 0:
        c.sort(key=lambda x:[1])
        print(c[0][0], c[-1][1])
        break
    else :
        d.sort(key=lambda x:[1])
        print(d[0][0], d[-1][1])
        break


