

def solution(n):
    answer = 0
    count = 0
    number = bin(n)

    for i in number:
        if i == "1":
          count+=1
    k = count

    while(True):
        n+=1
        count = 0
        if answer != 0:
            break
        b = bin(n)
        for i in b:
            if i == "1":
                count += 1
        b = count
        if k == b:
            answer = n

    return answer

solution(15)