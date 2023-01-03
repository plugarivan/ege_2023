'''
Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 10**6 символов.
Определите максимальное количество идущих подряд символов, среди которых не более двух точек.
'''
with open('../files/task24/24-181.txt') as f:
    s = f.readline()
    kmax = 0
    a = []
    for i in range(len(s)):
        if s[i] == '.':
            a.append(i)
    for i in range(len(a) - 3):
        kmax = max(kmax, a[i + 3] - a[i] - 1)
print(kmax)
