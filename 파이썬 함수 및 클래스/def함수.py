# 함수def
# 모바일 뱅킹 어카운트 만들기
def open_accout():
    print("새로운 계좌가 생성되었습니다.")

def deposit(blance,money):  # 잔액
    print("입금이 완료되었습니다.\n잔액은{0}원 입니다.".format(blance+money))
    return blance + money   # 리턴값을 함수 밖으로 내보냄
blance = 0


def whitdraw(blance,money):  # 잔액
    if blance >= money:
        print("출금이 완료되었습니다.\n"
              "잔액은{0}원 입니다.".format(blance-money))
    else:
        print("계좌에 돈이 충분하지 않습니다.\n"
              "잔액은{0}원 입니다.".format(blance))
    return blance - money   # 리턴값을 함수 밖으로 내보냄

blance = deposit(blance,1000)
print(blance)
blance = whitdraw(blance,2000)
print(blance)
