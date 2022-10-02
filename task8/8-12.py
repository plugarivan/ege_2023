'''
Вася составляет слова из букв слова БАРХАТКА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться
столько же раз, сколько в заданном слове. Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
Сколько различных слов может составить Вася?
'''
from itertools import permutations
words = permutations('бархатка')
s = set()
for w in words:
    word = ''.join(w)
    if word[0] in 'брхтк' and word[1] in 'а' and word[2] in 'брхтк' and word[3] in 'а' and word[4] in 'брхтк' and word[5] in 'а' and word[6] in 'брхтк' \
            and word[7] in 'а':
        s.add(word)
print(len(s))
