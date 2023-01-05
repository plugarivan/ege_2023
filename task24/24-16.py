'''
Текстовый файл 24-215.txt содержит строку из символов A, B, C и цифр 1, 2, 3, всего не более чем 10**6 символов.
Определите максимальное количество идущих подряд троек символов вида «цифра + буква + цифра».
'''
with open('../files/task24/24-215.txt') as f:
    s = f.readline()
    s = s.replace('A', 'b').replace('B', 'b').replace('C', 'b').replace('1', 'ch').replace('2', 'ch').replace('3', 'ch')
    s = s.replace('chbch', '*')
    k = kmax = 0
    for i in s:
        if i == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
print(kmax)