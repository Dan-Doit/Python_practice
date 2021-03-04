# 집합 (set)
# 중복 x 순서 x
my_set = {1,2,3,3,3}
print(my_set)        # 3이 중복이 안되게 출력됨

java = {"유재석","김태호","박명수"}
python = set(["유재석","박명수"])   # 세트 만들기

# 교집합 출력해보기(java 파이썬 둘다 출력)
print(java and python)
print(java.intersection(python)) # and와 같음

# 합집합(둘중에 하나라도 할수있는 사람)
print(java|python)
print(java.union(python))

# 차집합(java는 할수 있지만 python은 못하는 개발자)
print(java - python)
print(java.difference(python))

# 교육을 받아 python을 할줄 알게됨 김태호를 추가하자
print(java)
python.add("김태호")
# 까먹음
java.remove("박명수")

print(java,python)