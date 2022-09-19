'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются ещё несколько разрядов по следующему правилу: если N чётное, то к нему слева дописывается 10, а справа - 1, если N нечетное – слева дописывается 1 и справа 01;
3) Результат переводится в десятичную систему и выводится на экран.
Пример. Дано число N = 13. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1101.
2. Число нечетное, следовательно слева дописываем 1, справа 01 – 1+1101+01 = 1110101.
3. На экран выводится число 117.
В результате работы автомата на экране появилось число, большее 420. Для какого наименьшего значения N данная ситуация возможна?

'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s + '1'
    else:
        s = '1' + s + '01'
    if int(s, 2) > 420:
        print(n)
        break