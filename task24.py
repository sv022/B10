f = open('24.txt')
s = f.readline().strip()
for i in range(1000, 1, -1):
    for x in range(10):
        if str(x) * i in s:
            print(i)
            exit()
