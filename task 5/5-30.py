'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются ещё несколько разрядов по следующему правилу:
   а) если N чётное, то к нему справа приписывается в двоичном виде сумма цифр его двоичной записи;
   б) если N нечётное, то к нему справа приписываются два нуля, а слева единица.
Например, двоичная запись числа 1101 будет преобразована в 1110100.
Полученная таким образом запись (в ней как минимум на один разряд больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
Сколько существует различных чисел N, для которых результат работы данного алгоритма принадлежит отрезку [500; 700]?
'''
k = 0
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += bin(sum([int(i) for i in s]))[2:]
    else:
        s = '1' + s + '00'
    if 500 <= int(s, 2) <= 700:
        k += 1
print(k)
