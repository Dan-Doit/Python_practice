# while문
# 커피 안받으러 오면 버리기

starbucks = "토르"
index = 5
while index >= 1:
    print("{0}커피가 준비되었습니다 {1}번 남았어요.".format(starbucks,index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")

# # 받을때 까지 부르기(무한 루프)
# starbucks = "아이언맨"
# index = 1
# while True:
#     print("{0}커피가 준비되었습니다 {1}번 불렀습니다..".format(starbucks, index))
#     index += 1


# 손님이 올때까지 물어보기
customer = "마미손"
person = "Unknown"

while person != customer:
    print("{0}님의 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되시나요?")