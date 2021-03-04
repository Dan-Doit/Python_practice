
import collections


def solution(v):
    answer = []
    for i in zip(*v):
        y = collections.Counter(i)
        answer.extend([i for i in y if y[i] == 1])

    return answer

# 테스트 코드
v = [[1, 4], [3, 4], [3, 10]]

print(solution(v))


# x = [0,0]
# num = 0
# for i in zip(*v):
#     x[num] = sum(i)
#     num = num + 1
#
# a = [v[0][0],v[0][1]]
# b = [v[1][0],v[1][1]]
# c = [v[2][0],v[2][1]]
#
# if a[0] == b[0]:
#     x[0] = x[0] - (a[0]*2)
# elif a[0] == c[0]:
#     x[0] = x[0] - (a[0]*2)
# else:
#     x[0] = x[0] - (b[0]*2)
#
# if a[1] == b[1]:
#     x[1] = x[1] - (a[1]*2)
# elif a[1] == c[1]:
#     x[1] = x[1] - (a[1]*2)
# else:
#     x[1] = x[1] - (b[1]*2)
#
# print([x[0],x[1]])

