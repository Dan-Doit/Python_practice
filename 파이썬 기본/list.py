# 리스트

subway = [10,20,30]
print(subway)
subway = ["유재석","조세호","박명수"] # 서브웨이의 내용 수정
print(subway.index("유재석")) # 유재석이 몇번째 칸에 있는지 나옴 '0번째 칸'
# 다음 정류장에서 하하가 탐
subway.append("하하")
print(subway)
#다음 정류장에서 정형돈이 유재석과 조세호 사이에 탐
subway.insert(1,"정형돈")
print(subway)
subway.pop() # 가장 마지막부터 하나씩 뺌

print(subway.count("유재석")) #유재석이 몇명있는지
# 정렬
num = [1,3,2,5,4]
num.sort()   # 오름차순 정렬
print(num)
num.reverse()# 내림차순 정렬
print(num)

# 모두 지우기
num.clear()