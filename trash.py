def sem(a):
    s = ''
    while a > 0:
        s = str(a % 7) + s
        a //= 7
    return s

x = 7 ** 103 + 49 ** 98 - 7 ** 120 - 7 ** 33

for y in range(1, 10000):
    xy = int(sem(x)) + int(sem(y))
    if sum([int(i) for i in str(xy)]) < mini:
        mini
