
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]



def solution(array, commands):
    answer = []
    for i in commands:
        x,y,z = i
        answer.append(list(sorted(array[x-1:y]))[z-1])
    return answer

print(solution(array,commands))

