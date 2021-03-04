# if문
# 날씨 안내 프로그램
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("필요없어요!")

temp = int(input("오늘 기온 어때요? "))
if 30 <= temp:
    print("너무 더워요, 나가지마세요!")
elif temp < 30 and temp >= 10:
    print("적당한 날씨네요! 재밋게 노세요!")
elif 0 < temp < 10 :
    print("추워요 외투 챙기세요")
else:
    print("너무 추워요 나가면 안돼요!")