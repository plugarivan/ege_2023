'''
Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 10**6 символов.
Определите максимальное количество идущих подряд пар символов вида «согласная + гласная».
'''
with open('../files/task24/24-212.txt') as f:
    s = f.readline()
    s = s.replace('B', 'S').replace('C', 'S').replace('D', 'S').replace('A', 'G').replace('O', 'G')
    s = s.replace('SG', '*')
    k = kmax = 0
    for i in s:
        if i == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
print(kmax)