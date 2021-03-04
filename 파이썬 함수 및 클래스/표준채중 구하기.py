# Quiz 표준체중 구하는 함수
# 성별은 "남자" or "여자"
heigh = int(input("키를 입력해주세요(단위:cm)"))
gender = input("성별을 입력해주세요.")

def std_weight(heigh,gender):
    result = 0
    cm = float(heigh/100)
    if gender == "남자":
        result = float(cm * cm * 22)
        print("키 %dcm 남자의 표준체중은 %0.2f입니다."%(heigh,result))
    else:
        result = float(cm * cm * 21)
        print("키 %dcm 여자의 표준체중은 %0.2f입니다."%(heigh,result))

std_weight(heigh,gender)