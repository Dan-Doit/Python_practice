

arr = []

arr.append(0)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.pop()

print(arr[::-1])
print(arr)

from collections import deque
# 큐 구현을 위해 deque 덱 큐 라이브러리 사용 (일반 pop보다 속도면에서 빠름)
queue = deque()

queue.append(0)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀함수 (무한루프로 자기 자신을 호출하는 함수 따라서 탈출구도 필요함)
def recursive_function(i):
    if i == 100:
        return
    print(i,"번째 재귀함수에서", i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')
recursive_function(1)