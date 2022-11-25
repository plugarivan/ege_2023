with open('../files/task17/17-345.txt') as f:
    s = [int(x) for x in f]
    n = []
    sred = sum(s) / len(s)
    s52 = [x for x in s if x % 100 == 52]
    for i in range(len(s) - 1):
        if (s[i] < max(s52) - min(s52) and s[i + 1] >= max(s52) - min(s52)) or (s[i + 1] < max(s52) - min(s52) and s[i] >= max(s52) - min(s52)):
            n.append(s[i] + s[i + 1])
print(len(n), max(n))







