'''
Все 5-буквенные слова, составленные из букв слова ПАРУС записаны в алфавитном порядке и пронумерованы. Вот начало списка:

1. ААААА
2. ААААП
3. ААААР
4. ААААС
5. ААААУ
6. АААПА
...
Укажите номер первого слова в списке, начинающегося на У, в котором две буквы А не стоят рядом?

'''
from itertools import product
words = product('апрсу', repeat=5)
k = 0
for w in words:
    k += 1
    word = ''.join(w)
    if word[0] == 'у' and 'аа' not in word:
        print(word, k)
        break
