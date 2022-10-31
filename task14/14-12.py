'''
(П. Волгин) Значение выражения 8**888 + 15·15**1515 – 2**444 записали в системе счисления с основанием 8. Определите количество комбинаций цифр 7# в этой записи, где # – любая цифра от 1 до 6.
'''
k = 0
s = oct(8 ** 888 + 15 * 15 ** 1515 - 2 ** 444)[2:]
for i in range(len(s) - 1):
    if s[i] == '7' and s[i + 1] in '123456':
        k += 1
print(k)