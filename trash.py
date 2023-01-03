with open('files/task24/24-181.txt') as f:
    s = f.readline()
    kmax = 0
    for p in s.split('.'):
        if (p.count('A')  + p.count('E') + p.count('I') + p.count('O') + p.count('U') + p.count('Y')) <= 7:
            kmax = max(kmax, len(p))
print(kmax)