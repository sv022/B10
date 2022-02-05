n = 100000
s, ku, ke = 0, 0, 0
d = 10000
for _ in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    if (abs(a - b) % 41 != 0):
        d = min(d, abs(a - b))

if s % 41 == 0:
    print(s - d)
    exit()
print(s)        
