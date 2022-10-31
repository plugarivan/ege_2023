'''
Значение арифметического выражения: 36**17 + 6**66 – 216 записали в системе счисления с основанием 6. Сколько цифр «5» в этой записи?
'''
k = 0
x = 36 ** 17 + 6 ** 66 - 216
while x > 0:
    if x % 6 == 5:
        k += 1
    x //= 6
print(k)