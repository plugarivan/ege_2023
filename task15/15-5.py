'''
(М.В. Кузнецова) Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K (логическое «И» между соответствующими битами двоичной записи).
Определите наибольшее натуральное число A, такое что выражение

(((X & 13 ≠ 0) ∨ (X & A ≠ 0)) → (X & 13 ≠ 0)) ∨ ((X & A ≠ 0) ∧ (X & 39 = 0))
тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной X)?

'''
def f(x):
    return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))

for a in range(1, 1000):
    if all(f(x) == True for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
