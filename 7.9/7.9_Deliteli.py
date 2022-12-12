a = int(input())
b = int(input())
counter = 0
z = 0
for i in range(a, b + 1):
    for j in range(1, i+1):
        if i % j == 0:
            counter += j
        counter == z
        if counter > z:
            z = counter
            j1 = j
        if (j > j1) and (z == counter):
            j1 = j
    counter = 0
print(j1, z)
print()