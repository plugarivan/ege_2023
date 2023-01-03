'''
Текстовый файл 24.txt состоит не более чем из 10**6 символов X, Y и Z. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
with open('../files/task24/24.txt') as f:
    s = f.readline()
    k, kmax = 1, 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)
