p = set(range(1, 43))
q = set(range(25, 99))
a = set()
for x in range(-1000, 1000):
    if not((x in q) <= (not(x in p) and (x in q) <= (x in a))):
        a.add(x)
print(a)
print(max(a) - min(a))


