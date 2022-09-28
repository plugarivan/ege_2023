'''
Артур составляет 6-буквенные коды перестановкой букв слова КАБАЛА. При этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('кабала')
s = set()
for w in words:
    word = ''.join(w)
    if 'аа' not in word:
        s.add(word)
print(len(s))
