# 프린트 하는법
# way 1
print("나는 %s을 좋아해요."% "파이썬") # %문장의 값을 뒤에 문장으로 프린트함
print("나는 숫자%d을 좋아하고 %s 좋아해요."% (7,"python")) # %정수형은 d 문자형은 s 불리언은 b 등 많음
print("나는 숫자%s을 좋아해요." % 7) # 모든형을 s로 할수도 있다

# way 2
print("나는 {}을 좋아해요.".format("파이썬"))
print("나는 숫자{}을 좋아하고 {} 좋아해요.".format(7,"파이썬"))
print("나는 숫자{1}을 좋아하고 {0} 좋아해요.".format(7,"파이썬")) # 숫자를 사용해서 순서를 바꿔 출력도 가능

# way 3
print("나는 {age}살이고 ,{color}을 좋아해요.".format(age = 20 ,color = "blue")) # 변수로 만듬

# way 4
age = 10
color = "Red"
print(f"나는 {age}살이고, {color}를 좋아해요")