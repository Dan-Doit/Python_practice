# 서로 다른 문자열을 뒤집을 때 최소값 구하기 0과 1 이 들어감

arr = input()
count = 0
# 둘이 다른 문자열인지 확인
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]: # 원래 +1 을 쓰면 범위 밖이지만 위에 -1을 쓰면 딱여기까지 비교가됨
        count += 1
# 나누기 공식을 활용해 규칙구하기
if count % 2 == 0:
    count = count/2
else :
    count = (count/2) + 1

print(int(count))