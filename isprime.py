from itertools import combinations


def solution(nums):
    answer = 0
    z = 0
    count = 0
    arr = list(combinations(nums,3))
    b = 0

    for i in arr:
        for j in i:
            z += j
        for y in range(2,z):
            if z % y == 0:
                b = 1

        if b == 0:
            answer += 1
        else:
            b = 0

    return answer



print(solution([1,2,3,4]))
