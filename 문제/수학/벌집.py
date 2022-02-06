num = int(input())
count = 0
honeyComb = 1

while num > honeyComb:
    count += 1
    honeyComb += 6 * count

print(count+1)
