for i in range(1, 11):
    for j in range(1, 21):
        for k in range(2, 99, 2):
            if ((i * 10) + (j * 5) + (k * 0.5) == 100) and (i + j + k == 100):
                print(i, j, k)