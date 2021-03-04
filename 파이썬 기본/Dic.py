# 사전
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])            # 3번 키의 출력 get과 같음
print(cabinet.get(100))      # 100번 키의 출력 get을 쓰면 오류가 나지않고 None이 출력됨

# print(cabinet[5]) # 리스트에 5번 키가 없어서 에러가 남
print(cabinet.get(5)) # 에러 대신 None 출력
print(cabinet.get(5,"왜없어!")) # None 이라는 말대신 왜없어! 가 출력됨

# 사전 검색 법
print(3 in cabinet) # 3이 케비닛 안에 있어? 있으면 True 없으면 False

# 새 손님
cabinet["c-20"] = "조세호"  #키앖을 스트링형으로도 사용가능
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)
# 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)