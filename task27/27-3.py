with open('../files/task27/3/27-a.txt') as f:
    n = int(f.readline())
    summa, dmin = 0, 1000000000
    for i in range(n):
        a, b = map(int, f.readline().split())
        summa += max(a, b)
        d = abs(a - b)
        if d % 3 != 0:
            dmin = min(dmin, d)
    if summa % 3 != 0:
        print(summa)
    else:
        print(summa - dmin)
