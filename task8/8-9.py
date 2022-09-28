'''
Артур составляет 6-буквенные коды перестановкой букв слова ВОРОТА. При этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Артур?
'''
from itertools import permutations
words = permutations('ворота')
s = set()
for w in words:
    word = ''.join(w)
    if 'ао' not in word and 'оо' not in word and 'оа' not in word:
        s.add(word)
print(len(s))