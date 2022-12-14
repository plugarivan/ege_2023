'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:

F(0) = 1
F(n) = 1 + F(n - 1), если n > 0 и n нечётное
F(n) = F(n / 2) в остальных случаях
Определите количество значений n на отрезке [1, 500 000 000], для которых F(n) = 5.

'''
s = [1] * 500000000
for i in range(len(s)):
    if i > 0:
        if i % 2:
            s[i] = 1 + s[i - 1]
        else:
            s[i] = s[i // 2]


print(s.count(5))