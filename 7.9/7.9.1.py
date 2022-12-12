x1 = int(input())
x2 = int(input())
counter = 0
for i in range(x1, x2 + 1):
    for j in range(1, i+1):
        print(i, j)
print()