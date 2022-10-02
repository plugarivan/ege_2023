'''
Все 5-буквенные слова, составленные из букв А, О, У, записаны в обратном алфавитном порядке. Вот начало списка:

1. УУУУУ
2. УУУУО
3. УУУУА
4. УУУОУ
……
Запишите слово, которое стоит на 240-м месте от начала списка.

'''
from itertools import product
words = product('уоа', repeat=5)
s = []
for w in words:
    word = ''.join(w)
    s.append(word)
print(s[239])