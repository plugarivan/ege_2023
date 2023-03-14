with open('../files/task27/2/27-40a.txt') as f:
    n = int(f.readline())
    sumrez, s1, s2, mr = 0, 0, 0, 10001
    for i in range(n):
        a, b, c = map(int, f.readline().split())
        mx = max(a, b, c)
        mn = min(a, b, c)
        sred = (a + b + c) - mx - mn
        sumrez += mx
        s1 += mn
        s2 += sred
        if (mx - sred < mr) and ((mx - sred) % 2 != 0):
            mr = mx - sred
        if (mx - mn < mr) and ((mx - mn) % 2 != 0):
            mr = mx - mn
    if (s1 + s2) % 2 == 0:
        sumrez -= mr
print(sumrez)
