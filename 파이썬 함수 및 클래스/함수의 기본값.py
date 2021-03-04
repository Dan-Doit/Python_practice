# 함수의 기본값

# def profile(name,age,main_lang):
#     print("이름 : {0} \t나이 : {1}\t주 사용언어 : {2}"\
#           .format(name,age,main_lang))  # \한번은 아래문장과 하나이다 라고 해주는 말임
# profile("유재석","20","파이썬")
# profile("조세호", "10", "JAVA")

# 만약 같은학교 같은반 같은 수업이면 이미 알고있는 내용을 굳이 또 내보낼 필요가 없기에 기본 값을 지정해준다
# 기본값
# 기본값을 적어 놓으면 자료가 들어오지 않을경우 기본값으로 저장된 벨류가 프린트됨
def profile(name,age=17,main_lang="파이썬"):   # 기본값은 변수 옆에 = 으로 정한다
    print("이름 : {0} \t나이 : {1}\t주 사용언어 : {2}"\
          .format(name,age,main_lang))  # \한번은 아래문장과 하나이다 라고 해주는 말임

profile("유재석","20","파이썬")
profile("조세호", "10", "JAVA")

profile("유재석")
profile(("조세호"))