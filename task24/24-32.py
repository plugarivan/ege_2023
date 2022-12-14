'''
Текстовый файл 24-s2.txt состоит не более чем из 10**6 заглавных латинских букв. Определите символ, который чаще всего
встречается в файле сразу после буквы X. В ответе запишите сначала этот символ, а потом сразу (без разделителя)
сколько раз он встретился после буквы X. Если таких символов несколько, нужно вывести тот, который стоит раньше в алфавите.
Например, в тексте XBCXXBXDDD после буквы X два раза стоит B, по одному разу – X и D. Для этого текста ответом будет B2.
'''
with open('../files/task24/24-s2.txt') as f:
    s = f.readline()
    d = {}
    for i in range(len(s) - 2):
        if s[i] == 'X':
            key = s[i + 1]
            d[key] = d.get(key, 0) + 1
    Max = max(d.values())
    for x in d.items():
        if x[1] == Max:
            print(x)
