index, leng = map(int, input().split())


def loop(fruit, snake):
    minNum = min(fruit)

    if snake >= minNum:
        snake += 1
        fruit.remove(minNum)

        if len(fruit) != 0 and snake >= min(fruit):
            return loop(fruit, snake)
        else:
            return snake
    else:
        return snake

print(loop(list(map(int, input().split())), leng))
