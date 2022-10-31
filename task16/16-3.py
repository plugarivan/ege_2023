'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 2·n при n < 3
F(n) = 3·n + 5 +  F(n–2), если n ≥ 3 и чётно,
F(n) = n + 2·F(n–6), если n ≥ 3 и нечётно.
Чему равно значение функции F(61)?

'''
def f(n):
    if n < 3:
        return 2 * n
    else:
        if n % 2 == 0:
            return 3 * n + 5 + f(n - 2)
        else:
            return n + 2 * f(n - 6)

print(f(61))