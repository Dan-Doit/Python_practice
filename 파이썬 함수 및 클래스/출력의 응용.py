# 응용 프린트
print("python" + "JAVA")
print("python" , "JAVA")
print("python","JAVA",sep=" vs ")  # sep는 둘 사이에 어떤거를 넣을지 결정한다 , 단위
print("python","JAVA",sep=",",end="?") # 문장의 끝부분을 ?으로 바꾸어 주세요
print("무엇이 더 재미있을까요?")
print()

import sys
print("python" , "JAVA",file=sys.stdout) #표준 출력 처리(흰색)
print("python" , "JAVA",file=sys.stderr) #표준 에러 처리(붉은색)

score = {"수학" : 0, "영어" : 50, "코드" : 100}
for subject,score in score.items():    #items로 키랑 벨류 값음 앞에 두 변수에 입력
    # print(subject,score)
    print(subject.ljust(5), str(score).rjust(4))      # 왼쪽 정렬(5칸 확보),오른쪽 정렬(4칸 확보)

# 은행 대기 순번표
# 001,002,003 ...
for num in range(1,10):
    print("대기번호 :" + str(num).zfill(3)) # 3칸 문자열을 0으로 채움
print()
# 빈자리는 그냥두고, 한칸띄우고 오른쪽 정렬, 총 10자리 확보
print("{0: >10}".format(100))
# 양수일때는 + 음수일때는 -
print("{0: >+10}".format(100)) # 띄운 자리 옆에 +만 입력하면됨 - 는 그냥 -처리됨
print("{0: >+10}".format(-100))
# 왼쪽 정렬후 빈공간은 _로 채움
print("{0:_<+10}".format(100))
# 3자리마다 ,찍어주기
print("{0:,}".format(100000000))
# 3자리마다 콤마 찍고 부호도 삽입
print("{0:+,}".format(100000000))
# 3자리마다 콤마찍고 부호 붙이고 자릿수 확인 빈자리는 ^로 채우기
print("{0:^<+30,}".format(100000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 특정자리 소수점 보여주기
print("{0:.2f}".format(5/3))