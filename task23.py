a = [0] * 89
a[2] = 1

for i in range(2, 7):
    a[i + 2] += a[i]
    a[i * 2] += a[i]
    a[i * 3] += a[i]

for i in range(7, 89):
    a[i] = 0
    
for i in range(6, 28):
    a[i + 2] += a[i]
    a[i * 2] += a[i]
    a[i * 3] += a[i]
    
print(a[28])
