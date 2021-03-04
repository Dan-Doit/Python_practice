# 가변인자
# 고정값 외에 들어가야할 자료가 많고 양이 변칙적일때
def profile(name, age, *languege):
    print("이름 : {0} 나이 : {1}\t".format(name,age),end=" ")
    for i in languege:          # for문으로 반복 출력처리
        print(i,end=" ")
    print()

# 변수가 다르지만 하나의 함수로 사용이 가능하다.

profile("유재석",20,"파이썬","자바","C언어")
profile("조세호",21,"C++")

# 지역변수
# 함수 내에서만 사용가능
# 군대

gun = 10    # 지역변수 함수내에서는 쓸수없어
def checkpoint1(soldiers): # 경계근무
    gun = 20                           # 새로운 변수를 초기화 시켜 이함수 내에서만 씀 안그러면 이문장 안돌아감
    gun = gun - soldiers
    print("[함수내] 남은총 {}".format(gun))
print("[전체 총] : {}" .format(gun))
checkpoint1(2)  # 2명이 경계 근무 나감
print("[남은 총] : {}".format(gun))   #  ----> 에러남 왜냐하면 gun함수가 함수밖에있기때문

gun = 10    # 지금은 지역변수이다 하지만
def checkpoint2(soldiers):
    global gun    # 전체 영역에 있는 gun함수를 이함수에서 쓰겠다 라는뜻 이렇게 하면 밖의 gun도 영향을 받음
    gun = gun - soldiers
    print("[함수내] 남은총 {}".format(gun))
print("[전체 총] : {}" .format(gun))
checkpoint2(2)  # 2명이 경계 근무 나감
print("[남은 총] : {}".format(gun))  # 에러가 나지 않음 왜냐하면 gun을 전역변수 처리했기 때문

# 하지만 이런방식으로 하면 너무 코드가 복잡해지고 그렇게 때문에 보통 리턴을 시킨다.
def checkpoint3(gun, soldiers):
    gun = gun - soldiers
    print("[함수내] 남은총 {}".format(gun))
    return gun
print("[전체 총] : {}" .format(gun))
checkpoint3(10,2)  # 2명이 경계 근무 나감
print("[남은 총] : {}".format(gun))


