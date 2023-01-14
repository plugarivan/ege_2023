'''
(Б.С. Михлин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [586132; 586430],
числа, имеющие максимальное количество различных делителей. Найдите минимальное и максимальное из таких чисел.
В ответе для каждого из них запишите два числа: количество делителей и наибольший делитель, не равный самому числу.
'''
def divss(x):
    divs = set()
    for d in range(1, round(x ** 0.5) + 1):
        if x % d == 0:
            divs.add(d)
            divs.add(x // d)
    return sorted(divs)


maximum_divs = []
minimum_divs = []
for i in range(586132, 586431):
    if len(divss(i)) >= len(maximum_divs):
        maximum_divs = divss(i)
    if len(divss(i)) > len(minimum_divs):
        minimum_divs = divss(i)
print(len(minimum_divs), minimum_divs[-1], minimum_divs[-2])
print(len(maximum_divs), maximum_divs[-1], maximum_divs[-2])
