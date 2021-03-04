# countinue 문
# 선생님의 책읽기

absent = [2,5] #결석
no_book = [7]  # 책을 안가져 온사람

for student in range(1,11):
    if student in absent:
        continue                                  # 진행하지말고 처음으로 돌아가줘.
    elif student in no_book:
        print("오늘 수업은 여기까지할게! {0}번은 교무실로 따라와".format(no_book))
        break                                     # 뒤에부터는 반복문을 탈출한다.
    print("{0}번아 책좀 읽어줄래?".format(student))

