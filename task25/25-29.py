'''
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 10**8, найдите все числа, соответствующие маске 12*4?65, делящиеся на 161 без остатка.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 161.
'''
#1
for n in range(124065, 12994966):
    s = str(n)
    if s[:2] == '12' and s[-4] == '4' and s[-2:] == '65' and n % 161 == 0:
        print(n, n // 161)
#2
s1 = [''] + list(range(100))
s2 = list(range(10))
for x in s1:
    for y in s2:
        f = int(f'12{x}4{y}65')
        if f % 161 == 0:
            print(f, f // 161)
