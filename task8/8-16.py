'''
Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых ровно одна цифра 6,
при этом никакая нечётная цифра не стоит рядом с цифрой 6.
'''
from itertools import product
words = product('01234567', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if '16' not in word and '36' not in word and '56' not in word and '76' not in word and '61' not in word \
            and '63' not in word and '65' not in word and '67' not in word  and word.count('6') == 1 and word[0] != '0':
        k += 1
print(k)