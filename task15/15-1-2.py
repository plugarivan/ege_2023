'''
Укажите наименьшее целое значение А, при котором выражение

(3y + 2x < A) ∨ (x > 8) ∨ (y > 12)
истинно для любых целых положительных значений x и y.

'''
def f(x, y):
    return (3 * y + 2 * x < a) or (x > 8) or (y > 12)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
