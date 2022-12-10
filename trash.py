#19
def f(x, y, p):
    if x + y <= 30 and p == 2:
        return True
    else:
        if x + y > 30 and p == 2:
            return False
    return f(x - 1, y, p + 1) or f(x // 2 + 1, y, p + 1) or \
        f(x, y - 1, p + 1) or f(x, y // 2 + 1, p + 1)


print([i for i in range(100, 1, -1) if f(18, i, 0)])
#20
def f(x, y, p):
    if x + y <= 30 or p > 2:
        return p == 2
    if p % 2:
        return f(x - 1, y, p + 1) and f(x // 2 + 1, y, p + 1) and \
               f(x, y - 1, p + 1) and f(x, y // 2 + 1, p + 1)
    else:
        return f(x - 1, y, p + 1) or f(x // 2 + 1, y, p + 1) or \
        f(x, y - 1, p + 1) or f(x, y // 2 + 1, p + 1)


print(sorted([i for i in range(100, 1, -1) if f(18, i, 0)]))
#21
def f(x, y, p):
    if x + y <= 30 and (p == 2 or p == 4):
        return True
    else:
        if x + y > 30 and p == 4:
            return False
        else:
            if x + y <= 30:
                return False
    if p % 2 == 0:
        return f(x - 1, y, p + 1) and f(x / 2 + 1, y, p + 1) and \
               f(x, y - 1, p + 1) and f(x, y / 2 + 1, p + 1)
    else:
        return f(x - 1, y, p + 1) or f(x / 2 + 1, y, p + 1) or \
        f(x, y - 1, p + 1) or f(x, y / 2 +1, p + 1)


print(max([i for i in range(100, 1, -1) if f(18, i, 0)]))
