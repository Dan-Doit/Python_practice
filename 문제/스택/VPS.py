T = int(input())

for i in range(T):
    # 빈 스택을 만듭니다.
    Stack = []
    # VPS 를 받습니다.
    VPS = input()
    # for 문으로 괄호를 하나씩 비교합니다.
    for blank in VPS:
        if blank == '(':
            Stack.append(blank)
        elif blank == ')':
            if Stack:
                Stack.pop()
            else:
                print("NO")
                break
    # 스택에 값이 없어야 YES 가 프린트 됩니다.
    else:
        if not Stack:
            print("YES")
        else:
            print("NO")


# index = int(input())
#
# for _ in range(index):
#     VPS = input()
#     for _ in range(25):
#         VPS = VPS.replace('()', '')
#
#     if not VPS:
#         print('YES')
#     else:
#         print('NO')