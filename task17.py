f = open('17.txt')
a = [int(x) for x in f]
k, p = 0, 10_000_000
for i in range(1, len(a)):
    if a[i] >= 0 and a[i - 1] >= 0 and a[i] + a[i - 1] >= 50:
        k += 1
        p = min(p, a[i] * a[i - 1])
print(k, p)
