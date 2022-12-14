'''
(П. Финкель) Текстовый файл 24-228.txt состоит не более чем из 10**6 символов и содержит буквы английского алфавита и цифры.
Определите максимальное число в этом файле, ограниченное двумя парами символов XX и удовлетворяющее маске «3????78??45»,
где символ ? обозначает любую цифру. Пример такого числа: 31234781245. Найдите сумму нечётных цифр и произведение
чётных цифр найденного числа, запишите в качестве ответа сумму этих двух чисел.
'''
with open('../files/task24/24-228.txt') as f:
    groups = f.readline().split('XX')[1:-1]
    ans = []
    chifri = '0123456789'
    for x in groups:
        if len(x) == 11 and x[0] == '3' and x[5:7] == '78' and x[-2:] == '45' \
                and x[1] in chifri and x[2] in chifri and x[3] in chifri and x[4] in chifri \
                and x[-3] in chifri and x[-4] in chifri:
           ans.append(x)
    pr, summa = 1, 0
    for i in max(ans):
        if int(i) % 2 == 0:
            pr *= int(i)
        else:
            summa += int(i)
print(pr + summa)