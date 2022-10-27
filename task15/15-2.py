'''
Укажите наименьшее целое значение А, при котором выражение

(y + 3x < A) ∨ (x > 9) ∨ (y > 20)
истинно для любых целых положительных значений x и y.
'''
def f(x, y):
    return (y + 3 * x < a) or (x > 9) or (y > 20)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break