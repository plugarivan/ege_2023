'''
Значение выражения 343**1515 – 6∙49**1520 + 5∙49**1510 – 3∙7**1530 – 1550 записали в системе счисления с основанием 7. Определите количество значащих нулей в этой записи.
'''
k = 0
x = 343 ** 1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 1550
while x > 0:
    if x % 7 == 0:
        k += 1
    x //= 7
print(k)