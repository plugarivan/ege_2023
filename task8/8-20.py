'''
Все 4-буквенные слова, составленные из букв М, А, Р, Т, записаны в алфавитном порядке. Вот начало списка:

1. АААА
2. АААМ
3. АААР
4. АААТ
...
Какое количество слов находятся между словами МАРТ и РАМТ (включая эти слова)?

'''
from itertools import product
words = product('амрт', repeat=4)
s = []
for w in words:
    word = ''.join(w)
    s.append(word)
print(s.index('рамт') - s.index('март') + 1)
