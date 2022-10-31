'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = 1, при n < 2,
F(n) = F(n/3) - 1, когда n ≥ 2 и делится на 3,
F(n) = F(n - 1) + 17, когда n ≥ 2 и не делится на 3.
Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 43.

'''
s = 100000 * [1]
for i in range(len(s)):
    if i >= 2:
        if i % 3 == 0:
            s[i] = s[i // 3] - 1
        else:
            s[i] = s[i - 1] + 17

print(s.count(43))