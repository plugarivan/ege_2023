'''
Вася составляет слова из букв слова АВТОРОТА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться
столько же раз, сколько в заданном слове. Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
Сколько различных слов может составить Вася?
'''
from itertools import permutations
words = permutations('авторота')
k = set()
for i in words:
    word = ''.join(i)
    s = ''
    for c in word:
        if c in 'ао':
            s += 'g'
        else:
            s += 's'
    if 'gg' not in s and 'ss' not in s:
        k.add(word)
print(len(k))

