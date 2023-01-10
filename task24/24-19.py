'''
(П. Финкель) Текстовый файл 24-230.txt состоит не более чем из 10**6 символов и содержит буквы английского алфавита и цифры.
Определите максимальное число в этом файле, ограниченное двумя парами символов ZZ и удовлетворяющее маске «8???54???22»,
где символ ? обозначает любую цифру. Пример такого числа: 81235412322. Найдите произведение нечётных цифр найденного числа.
'''
with open('../files/task24/24-230.txt') as f:
    groups = f.readline().split('ZZ')[1:-1]
    ans = []
    chifri = '0123456789'
    for x in groups:
        if len(x) == 11 and x[0] == '8' and x[4:6] == '54' and x[-2:] == '22' \
                and x[1] in chifri and x[2] in chifri and x[3] in chifri and x[6] in chifri and x[7] in chifri \
                and x[8] in chifri:
            ans.append(x)
pr = 1
for i in max(ans):
    if int(i) % 2:
        pr *= int(i)
print(pr)

