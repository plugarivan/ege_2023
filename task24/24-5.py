'''
(А.М. Кабанов) В текстовом файле k7a-3.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F (в произвольном порядке).
'''
with open('../files/task24/k7a-3.txt') as f:
    s = f.readline()
    k = kmax = 0
    for i in s:
        if i in 'ABEF':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
print(kmax)
