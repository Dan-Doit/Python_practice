from sys import stdin


def push(stack, val):
    stack.append(val)


def pop(stack):
    if stack:
        return stack.pop()
    else:
        return -1


def size(stack):
    return len(stack)


def empty(stack):
    if stack:
        return 0
    else:
        return 1


def top(stack):
    if stack:
        return stack[len(stack) - 1]
    else:
        return -1


array = []
for i in range(int(stdin.readline())):
    action = stdin.readline()
    print(action)
    if action == 'pop':
        print(pop(array))
    elif action == 'size':
        print(size(array))
    elif action == 'empty':
        print(empty(array))
    elif action == 'top':
        print(top(array))
    else:
        push(array, action.split(' ')[1])
