# 자료구조(list, tuple, dic, set) 변경
# 커피숍

menu = {"커피","우유","주스"}
print(type(menu))

menu = list(menu)
print(type(menu))

menu = tuple(menu)
print(type(menu))

# Quiz (당첨자 뽑기)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)            # list 안을 섞어줌
print(lst)
sample(lst,1)           # 아무나 변수(한명)을 뽑음
print(sample(lst,1))

# 유저 만들기
users = range(1,21)
users = list(users) # 리스트로 바꾸자
print(users)

shuffle(users)
winners = sample(users,4)

print("------당첨자 발표------")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("--축하합니다--")