k = 0
for i in range(550_001, 650_000):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            t = (i // j)
            for u in range(2, int(t ** 0.5) + 1):
                if t % u == 0:
                    print(i, t)
                    k += 1
                    break
            break
    if k == 6:
        break
