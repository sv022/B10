def F(x, y, a):
    return (x >= a) or (y >= a) or (x * y <= 270)

for a in range(300, 1, -1):
    fl = False
    for x in range(1, 300):
        for y in range(1, 300):
            if not F(x, y, a):
                fl = True
        if fl:
            break
    if fl:
        continue
    else:
        print(a)
        break
