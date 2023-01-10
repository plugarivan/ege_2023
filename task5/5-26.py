'''
Автомат обрабатывает натуральное число N > 1 по следующему алгоритму:
1) Строится двоичная запись числа N.
2) В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3) В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Вторая справа цифра 1, новая запись 101112.
3) Вторая слева цифра 0, новая запись 1011102.
4) Десятичное значение полученного числа 46.
При каком наименьшем числе N в результате работы алгоритма получится R > 210? В ответе запишите это число в десятичной системе счисления.
'''
for n in range(2, 200):
    s = bin(n)[2:]
    s += s[-2]
    s += s[1]
    if int(s, 2) > 210:
        print(n)
        break