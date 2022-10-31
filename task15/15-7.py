'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа А формула

(ДЕЛ(x, A) ∧ ¬ДЕЛ(x, 36)) → ¬ДЕЛ(x, 12)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

'''
def f(x):
    return ((x % a == 0) and (x % 36 != 0)) <= (x % 12 != 0)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break