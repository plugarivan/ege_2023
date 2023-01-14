'''
(К. Багдасарян) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
- символ «Ч» означает ровно одну произвольную четную цифру;
- символ «Н» означает ровно одну произвольную нечетную цифру;
Например, маске ЧН2 соответствуют числа 232, 612, 692 и т.д. Среди натуральных чисел, не превышающих 10**7, найдите все числа,
соответствующие маске 1ЧНЧНЧН, делящиеся на 4023 без остатка. В ответе запишите в первом столбце таблицы все найденные
 числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 4023.
'''
for i in range(1000000, 2000000):
    s = str(i)
    chet = '02468'
    nechet = '13579'
    if s[0] == '1' and s[1] in chet and s[2] in nechet and s[3] in chet and s[4] in nechet and s[5] in chet and s[6] in nechet and i % 4023 == 0:
        print(i, i // 4023)