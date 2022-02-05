k = 0
for x in range(1000, 9999):
    x = str(x)
    if (x[0] == x[1] and x[2] != x[0] and x[3] != x[0] and x[2] != x[3]) or \
        ((x[1] == x[2]) and x[0] != x[1] and x[3] != x[1] and x[0] != x[3]) or \
            ((x[2] == x[3]) and x[0] != x[2] and x[1] != x[2] and x[0] != x[1]):
                print(x)
                k += 1
print(k)
