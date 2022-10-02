'''
(Е. Джобс) Петя составляет пятибуквенные слова из букв слова УЖЕМАЙ и записывает их в алфавитном порядке в список. Вот начало списка

1. ААААА
2. ААААЕ
3. ААААЖ
4. ААААЙ
5. ААААМ
6. ААААУ
7. АААЕА
...
Сколько существует слов, стоящих в списке на позициях с чётными номерами, в которых нет двух одинаковых подряд идущих букв?

'''
from itertools import product
words = product('аежйму', repeat=5)
k = 0
count = 0
for w in words:
    k += 1
    word = ''.join(w)
    if k % 2 == 0 and 'аа' not in word and 'ее' not in word and 'жж' not in word and 'йй' not in word and 'мм' not in word and 'уу' not in word:
        count += 1
print(count)