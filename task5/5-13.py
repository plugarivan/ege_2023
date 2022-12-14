'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
Сколько различных чисел, принадлежащих отрезку [20; 50], могут появиться на экране в результате работы автомата?
'''
k = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if 20 <= int(s, 2) <= 50:
        k.add(int(s, 2))
print(len(k))
