'''
(Б.С. Михлин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [286564; 287270], числа,
имеющие максимальное количество различных делителей. Если таких чисел несколько, то найдите максимальное из них.
В ответе запишите два числа: количество делителей найденного числа и его наибольший делитель, не равный самому числу.
'''
def divss(x):
    divs = set()
    for d in range(1, round(x ** 0.5) + 1):
        if x % d == 0:
            divs.add(d)
            divs.add(x // d)
    return sorted(divs)


maximum_divs = []
for i in range(286564, 287271):
    if len(divss(i)) >= len(maximum_divs):
        maximum_divs = divss(i)
print(len(maximum_divs), maximum_divs[-1], maximum_divs[-2])
