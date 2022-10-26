'''
На числовой прямой даны три отрезка: P = [20, 30], Q = [5, 15] и R = [35,50]. Какова наименьшая длина отрезка A, при котором формула

((x ∈ P) → (x ∈ Q)) ∨ (¬(x ∈ A) → (x ∈ R))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

'''
p = set(range(20, 31))
q = set(range(5, 16))
r = set(range(35, 51))
a = set()
for x in range(-1000, 1000):
    if not(((x in p) <= (x in q)) or ((x not in a) <= (x in r))):
        a.add(x)
print(max(a) - min(a))
print(a)
