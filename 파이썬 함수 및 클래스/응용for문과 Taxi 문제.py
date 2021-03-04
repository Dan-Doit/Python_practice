# 출석번호의 앞에 100을 붙이기로함
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
student = ["Iron Man","Thor","I am Groot"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["Iron Man","Thor","I am Groot"]
student = [i.upper() for i in student]
print(student)

# Quiz
# 택시 승객 받기(50명승객 난수 5~15분사이의 승객만 받기)
from random import *
ran = 0
count = 0
ox = "O"
for i in range(1,51): # 총 탑승하시는분
   ran = randint(1,50) # 몇분 걸리는지 랜덤으로 산출
   if 4 < ran < 16:   # 만약 5~15분 사이이 고객이라면
        print("[{0}] {1}째 손님 (소요시간 : {2}분)".format(ox,i,ran))
        count += 1 # 받은 고객 카운트
        continue
   print("[ ] {1}째 손님 (소요시간 : {2}분)".format(ox,i,ran))
print("총 탑승 고객 : {0}명".format(count))