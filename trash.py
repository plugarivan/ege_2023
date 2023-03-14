for n in range(1263050, 129963960):
    s = str(n)
    if s[:2] == '12' and s[-5:-3] == '63' and s[-2] == '5' and n % 3123 == 0:
        print(n)

