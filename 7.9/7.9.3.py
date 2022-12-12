x1 = int(input())
while x1 > 9:
    counter = 0
    while x1 > 0:
        y1 = x1 % 10
        counter += y1
        x1 = x1 // 10
    x1 = counter
print(x1)