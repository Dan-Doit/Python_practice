# 일반가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*10000))

# 조조할인 가격
def price_mo(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*60000))

# 군인 할인
def price_so(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*40000))

    # 이런 함수들이 모인걸 모듈이라고 한다.
    # 이것들이 또 모인걸 패키지라고 한다.
