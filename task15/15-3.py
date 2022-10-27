'''
Укажите наибольшее целое значение А, при котором выражение

(y + 3x ≠ 60) ∨ (2x > A) ∨ (y > A)
истинно для любых целых положительных значений x и y.

'''
def f(x, y):
    return (y + 3 * x != 60) or (2 * x > a) or (y > a)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
