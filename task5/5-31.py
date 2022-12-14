'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются ещё несколько разрядов по следующему правилу: если N чётное, то к нему слева дописывается 1, а справа - 10, если N нечетное – слева дописывается 11 и справа 0;
3) Результат переводится в десятичную систему и выводится на экран.
Пример. Дано число N = 13. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1101.
2. Число нечетное, следовательно слева дописываем 11, справа 0 – 11+1101+0 = 1111010.
3. На экран выводится число 122.
Сколько различных результатов, принадлежащих отрезку [800; 1500], может быть получено в результате работы автомата?
'''
mn = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '10'
    else:
        s = '11' + s + '0'
    if 800 <= int(s, 2) <= 1500:
        mn.add(s)
print(len(mn))
