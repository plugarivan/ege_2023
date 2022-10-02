'''
Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 8 цифр, причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
k = 0
chet = '02468'
nechet = '13579'
for i in range(10000000, 100000000, 5):
    x = str(i)
    if len(x) == len(set(x)) and ((x[0] in chet and x[1] in nechet and x[2] in chet and x[3] in nechet and x[4] in chet and x[5] in nechet and x[6] in chet and x[7] in nechet) or \
            (x[0] in nechet and x[1] in chet and x[2] in nechet and x[3] in chet and x[4] in nechet and x[5] in chet and x[6] in nechet and x[7] in chet)):
        k += 1
print(k)
