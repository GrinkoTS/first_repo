for a in range(1, 151):
    qa = a ** 5
    for b in range(a, 151):
        qb = b ** 5
        for c in range(b, 151):
            qc = c ** 5
            for d in range (c, 151):
                qd = d ** 5
                for e in range(d, 151):
                    qe = e ** 5
                    if (qa + qb + qc + qd == qe):
                        print(a + b + c + d + e)