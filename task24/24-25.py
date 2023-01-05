'''
Текстовый файл 24-s1.txt состоит не более чем из 10**6 заглавных латинских букв (A..Z). Текст разбит на строки различной длины.
Определите количество строк, в которых буква S встречается столько же раз, сколько и буква X.
'''
with open('../files/task24/24-s1.txt') as f:
    k = 0
    for s in f:
        if s.count('S') == s.count('X'):
            k += 1
print(k)