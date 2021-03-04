# Random 변수 불러오기
# 복권 번호 생성기
from random import *

print(int(random()))   # random 은 0~1의 실수를 내보내기 때문에 정수형을 덮어준다.
print(randint(1,45))  # int는 숫자를쓴 범위로 1이상 45이하 나온다.
print(randrange(1,46)) # range 는 1~46 미만의 숫자가 나온다.

# 슬라이스
# 문자열의 자신이 필요한 정보 얻기
jumin = "930501-1234567"
print("성별은 " +jumin[7])
print("연 " +jumin[0:2])  # 0부터 2 직전까지 출력
print("월 " +jumin[2:4])
print("일 " +jumin[4:6])
print("주민 뒷자리 " +jumin[7:]) # 7번째 부터 끝까지 나옴, 처음부터도 가능하다
print("뒷자리 거꾸로 " + jumin[-7:]) # 7번째 부터 마지막까지 중요한점은 - 라는점!