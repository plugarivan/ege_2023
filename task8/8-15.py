'''
Определите количество пятизначных чисел, записанных в девятеричной системе счисления, которые не начинаются с нечётных
цифр, не оканчиваются цифрами 1 или 8, а также содержат в своей записи не более одной цифры 3.
'''
from itertools import product
words = product('012345678', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if word[0] not in '01357' and word[-1] not in '18' and word.count('3') <= 1:
        k += 1
print(k)