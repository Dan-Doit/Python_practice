import heapq

def solution(jobs):
    n = len(jobs)

    heapq.heapify(jobs)
    current, length = heapq.heappop(jobs)
    answer = 0
    pq = []

    heapq.heappush(pq,(current + length, current, length))

    while pq:
        current,start,length = heapq.heappop(pq)
        answer = answer - start + current
        while pq:
            _,c,d = heapq.heappop(pq)
            heapq.heappush(jobs,[c,d])
        while jobs:
            if jobs[0][0] > current:
                if not pq:
                    e,f = heapq.heappop(jobs)
                    heapq.heappush(pq,(e+f,e,f))
                break
            else:
                a,b = heapq.heappop(jobs)
                heapq.heappush(pq,(current + b, a, b))
    answer /= n
    print(int(answer))
    return int(answer)

solution([[0,3],[1,6],[3,8]])