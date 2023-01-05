'''
(А.М. Кабанов) В текстовом файле k7a-6.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, не содержащей гласных букв.
'''
with open('../files/task24/k7a-6.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in s:
        if i not in 'AE':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
print(kmax)