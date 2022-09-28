'''
Из букв слова Р А Д У Г А составляются 6-буквенные последовательности. Сколько можно составить различных последовательностей,
если известно, что в каждой из них содержится не менее 3 согласных?
'''
from itertools import product
words = product('радуг', repeat=6)
k = 0
for w in words:
    word = ''.join(w)
    if (word.count('р') + word.count('д') + word.count('г')) >= 3:
        k += 1
print(k)
