
from itertools import combinations, count
from collections import Counter


def solution(orders, course):
    recor = []
    answer = []
    foods = Counter({})
    for i in orders:
        recor.append(list(map(str, i)))

    # 가능한 모든 배열의 조합 만들기
    def select(recor, k):
        for i in recor:
            for j in list(combinations(i, k)):
                foods["".join(j)] += 1

    # 딕셔너리를 구하기위한 빈 딕셔너리 값
    close = {}
    ans = {}

    for i in course:
        # combinations 함수를 이용해 코스만큼 조합하기
        select(recor, i)
        # 글자별로 다시 딕셔너리 구현하기
        close = {key: value for key, value in foods.items() if len(key) == i}
        # 밸류값이 가장큰 것 찾기
        max_food = max(close.values())
        # 가장큰 밸류 값으로 다시 정리
        ans = {key: value for key, value in close.items() if value == max_food}
        # 들어있는 키 값을 답에 정리
        answer += ans.keys()

    # 들어있는 함수를 글자순서로 정리하기
    answer.sort()
    print(answer)

    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])