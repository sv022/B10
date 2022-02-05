def P(n, o, res=''):
    while n != 0:
        res += str(n % o)
        n = n // o
    return res[::-1]

def F(n):
    n = n - (n % 8) + (n % 2)
    r = P(n, 2)
    if r.count('1') % 2 == 0:
        r += '00'
    else:
        r += '10'
    return int(r, base=2)

for i in range(20, 91):
    if F(i) > 97:
        print(F(i))
        break
