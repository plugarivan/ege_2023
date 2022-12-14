'''
На числовой прямой даны два отрезка: P = [10, 40] и Q = [25, 35]. Найдите наибольшую возможную длину отрезка A, при котором формула

( (x ∈ А) ∧ (x ∉ P) ) → (x ∈ Q)
тождественно истинна, то есть принимает значение 1 при любых x.

'''
p = set(range(10, 41))
q = set(range(25, 36))
a = set(range(-1000, 1000))
for x in range(-1000, 1000):
    if not(((x in a) and (x not in p)) <= (x in q)):
        a.remove(x)
print(max(a) - min(a))
print(a)
