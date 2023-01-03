'''
Текстовый файл 24-1.txt содержит только заглавные буквы латинского алфавита (ABC…Z).
Определите максимальное количество идущих подряд символов, среди которых буква A встречается не более пяти раз.
'''
with open('../files/task24/24-1.txt') as f:
    s = f.readline()
    kmax = 0
    a = []
    for i in range(len(s)):
        if s[i] == 'A':
            a.append(i)
    for i in range(len(a) - 6):
        kmax = max(kmax, a[i + 6] - a[i] - 1)
print(kmax)