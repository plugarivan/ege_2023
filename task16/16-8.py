'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = n, при n ≤ 3
при n > 3:
  F(n) = 2*n*n + F(n–1), при чётном n;
  F(n) = n*n*n + n + F(n–1), при нечётном n;
Определите количество натуральных значений n, при которых F(n) меньше, чем 107.

'''
s = [0] * 10 ** 5
for i in range(len(s)):
    if i <= 3:
        s[i] = i
    else:
        if i % 2:
            s[i] = i * i * i + i + s[i - 1]
        else:
            s[i] = 2 * i * i + s[i - 1]

print(len([n for n in range(len(s)) if 1 <= s[n] < 10 ** 7]))

