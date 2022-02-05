def P(n, o, res=''):
    while n != 0:
        res += str(n % o)
        n = n // o
    return res[::-1]

s = 5 ** 90 - 5 ** 80 + 25 ** 12 - 125

print(P(s, 5).count('4'))
