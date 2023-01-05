'''
(П.Е. Финкель) Текстовый файл 24-1.txt состоит не более чем из 10**6 символов - заглавных латинских букв и цифр.
Определите максимальное число, состоящее только из нечётных цифр. Под числом подразумевается последовательность цифр,
ограниченная другими символами (не цифрами).
'''
with open('../files/task24/24-1.txt') as f:
    s = f.readline()
    s1 = ''
    numbers = []
    maximum = 0
    for c in s:
        if c.isdigit():
            s1 += c
        else:
            if s1 != '':
                numbers.append(s1)
            s1 = ''
    for i in numbers:
        nechet = len([x for x in i if int(x) % 2])
        if nechet == len(i):
            maximum = max(maximum, int(i))
print(maximum)
