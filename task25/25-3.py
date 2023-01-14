'''
(А.Н. Носкин) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [190061; 190072], числа,
имеющие ровно 4 различных НЕЧЁТНЫХ делителя. В ответе для каждого найденного числа запишите два его наибольших нечётных делителя в порядке убывания.
'''
for i in range(190061, 190073):
    divs = []
    for d in range(1, i + 1):
        if i % d == 0 and d % 2:
            divs.append(d)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(sorted(divs, reverse=True)[:2])
