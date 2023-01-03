'''
(А. Брейк) Непоседливый Непоседа решил сыграть в игру. Он придумал исполнителя, преобразующего числа на доске и имеющего три команды:
1. Прибавь 3
2. Сделай чётное
3. Сделай нечётное
Первая команда увеличивает число на 3, вторая команда преобразует число N в число 2N при условии, что оно является нечетным.
Третья — преобразует четное число N в нечетное вида 2N+1. Сколько существует программ, которые преобразуют исходное число 1 в 76,
а траектория вычислений программы содержит не более пяти преобразований в чётное?
'''
def f(x, y, k):
    if x > y:
        return 0
    if x == y:
        return 1
    if x % 2 and k < 5:
        return f(x + 3, y, k) + f(x * 2, y, k + 1)
    else:
        return f(x + 3, y, k) + f((x * 2) + 1, y, k)

print(f(1, 76, 0))