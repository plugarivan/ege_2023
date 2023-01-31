'''
Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 5 цифр, причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import product
words = product('0123456789', repeat=5)
k = set()
for i in words:
    word = ''.join(i)
    s = ''
    for c in word:
        if c in '02468':
            s += 'ч'
        else:
            s += 'н'
    if 'чч' not in s and 'нн' not in s and word[0] != '0' and word[-1] in '50' \
            and len(set(word)) == 5:
        k.add(word)
print(len(k))
