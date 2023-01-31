'''
Из букв А З И М У Т составляются 6-буквенные последовательности.
Сколько можно составить различных последовательностей, если известно, что в каждой из них содержится не менее 3 согласных?
'''
from itertools import product
words = product('азимут', repeat=6)
k = 0
for i in words:
    word = ''.join(i)
    if (word.count('з') + word.count('м') + word.count('т')) >= 3:
        k += 1
print(k)

