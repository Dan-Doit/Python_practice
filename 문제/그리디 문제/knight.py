d = [[2, 0], [-2, 0], [0, -2], [-2, -2]]

x = [1, -1]

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = 0
y = 0

knight = input()

for i in range(len(alpha)):
    if knight[0] == alpha[i]:
        x = int(knight[1])
        y = i + 1

for i in d:
    if