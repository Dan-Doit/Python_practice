# # 예외처리
# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 값을 입력해주세요"))
#     num2 = int(input("두번째 값을 입력해주세요"))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("값이 잘못되었어요. 숫자를 입력해주세요")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알수없는 오류가 발생하였습니다.")
#     print(err)
# # int 값이 아니면 에러가남 그래서 해주는 것이 예외처리 try,

# 예외처리
class bignumerr (Exception):   # Exception 클래스를 상속받음
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 값을 입력해주세요"))
    num2 = int(input("두번째 값을 입력해주세요"))
    if num1 >= 10 or num2 >= 10 :
        raise bignumerr("입력값 : {0},{1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력해주세요")
except bignumerr as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력해 주세요")
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다.")
# int 값이 아니면 에러가남 그래서 해주는 것이 예외처리 try,except