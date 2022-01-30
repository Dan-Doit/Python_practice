from collections import deque

# 카드 를 만든다.
num = [i + 1 for i in range(int(input()))]
# 큐 형태로 변환한다.
queue = deque(num)
# 제일 앞 카드 꺼네기
while len(queue) != 1:
    # 첫번째 카드 버리기
    queue.popleft()
    # 두번째 카드 맨 위로 올리기
    drawCard = queue.popleft()
    queue.append(drawCard)
print(queue[0])


# n, k = input().split(' ')
# k = int(k) - 1
# newK = k
# yosepus = []
# numbers = [i + 1 for i in range(int(n))]
#
# while len(numbers) != 1:
#     print(newK)
#     popValue = numbers.pop(newK)
#     yosepus.append(popValue)
#
#     newK = newK + k - len(numbers) if newK + k > len(numbers) else newK + k
#
# print(yosepus)