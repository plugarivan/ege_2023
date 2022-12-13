def f(x, y, k=0):
    if x > y:
        return 0
    if x == y:
        return 1
    if x % 2:
        return f(x + 3, y, k) + f(x * 2, y, k + 1)
    else:
        return f(x + 3, y, k) + f((x * 2) + 1, y, k)

print(f(1, 76, 0))