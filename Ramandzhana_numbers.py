for a in range(1, 35):
    qa = a ** 3
    for b in range(a, 35):
        qb = b ** 3
        for c in range(1, 35):
            qc = c ** 3
            for d in range (c, 35):
                qd = d ** 3
                if ((qa + qb) == (qc + qd)) and (qa + qb) >= 1729 and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(qa + qb)