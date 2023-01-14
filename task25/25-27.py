'''
Пусть N(k) = 19 500 000 + k, где k – натуральное число. Найдите пять наименьших значений k, при которых N(k) нельзя
представить в виде произведения трёх натуральных чисел, больших 1. В ответе запишите найденные значения k в порядке
убывания, справа от каждого значения запишите наибольший делитель N(k), не равный самому числу.
'''


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

k = 1
count = 0
while count != 5:
    flag = True
    n = div(19500000 + k)
    for i1 in range(len(n)):
        for i2 in range(i1 + 1, len(n)):
            for i3 in range(i2 + 1, len(n)):
                if (19500000 + k) == (n[i1] * n[i2] * n[i3]):
                    flag = False
    if flag:
        count += 1
        print(k, max(n))
    k += 1
