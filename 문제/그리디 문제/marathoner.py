
from collections import Counter

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(participant)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]

def solution(participant, completion):
    answer = ""
    par = Counter({})
    for i in participant:
        par[i] += 1
    for i in completion:
        par[i] -= 1
    for i in participant:
        if par[i] == 1:
            return i
            break


# def solution(s,c):
#
#     s.sort()
#     c.sort()
#
#     for par, com in zip(s, c) :
#         if par != com :
#             return par
#
#     return s[-1]

par = ["mislav", "stanko", "mislav", "ana"]

com = ["stanko", "ana", "mislav"]

print(solution(par,com))