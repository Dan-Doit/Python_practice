index, init_snake = map(int, input().split())

fruit = list(map(int, input().split()))


def loop(sorted_fruit, snake):
    for i in sorted(sorted_fruit):
        if snake >= i:
            snake += 1
    return snake


print(loop(fruit, init_snake))
