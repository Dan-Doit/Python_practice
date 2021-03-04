# 대소문자 구별
python = "Python is Amazing"

print(python.lower())  # 전체를 소문자로 바꾸어줌
print(python.upper())  # 전체를 대문자로 바꾸어줌
print(python[0].isupper())  # 0번째 인덱스가 대문자인지 물어보는 함수!
print(len(python))     # 숫자세기
print(python.replace("Python","JAVA")) # 원하는 문자열을 바꾸어준다. 대소문자 구별해야함

index = python.index("n")  # 문자열의 인덱스를 찾아줌
print(index)
index = python.index("n",index + 1) # 이렇게 하면 2번째 인덱스를 찾아줌!
print(index)

print(python.find("JAVA")) # find와 index는 기능은 같지만 find는 못찾을시 -1을 출력함
print(python.count("n")) # 문자열내에 특정문자가 몇개인지 확인