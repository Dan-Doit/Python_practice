from itertools import combinations

def solution(M, load):
    count = len(load)
    now = sorted(load)
    ans = 0
    while True:

        flag = False

        if count == 0:
            if len(now) > 0:
                ans = -1
                break
            else:
                break

        select = list(combinations(now, count))
        select.reverse()
        print(select)
        for arr in select:
            sum = 0
            for i in arr:
                sum = sum + i
            if sum <= M:
                ans += 1
                for i in arr:
                    for j in range(len(now)):
                        if i == now[j]:
                            now.pop(j)
                            flag = True
                            break
                if flag: break
            if flag: break
        if flag:
            count = count
        else:
            count = count - 1
    return ans

print(solution(10,[2,3,7,8]))
