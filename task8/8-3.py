'''
Василий составляет 4-буквенные коды из букв А, Р, С, Е, Н, И, Й. Каждую букву можно использовать любое количество раз,
при этом код не может начинаться с буквы Й и должен содержать хотя бы одну гласную. Сколько различных кодов может составить Василий?
'''
from itertools import product
words = product('арсений', repeat=4)
k = 0
for w in words:
    word = ''.join(w)
    if word[0] != 'й' and (word.count('а') + word.count('е') + word.count('и')) >= 1:
        k += 1
print(k)
