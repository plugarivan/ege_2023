'''
Исполнитель преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Умножь на 3
3. Умножь на 4
Первая команда увеличивает число на экране на 1, вторая умножает его на 3, третья – умножает на 4. Сколько существует различных программ,
которые преобразуют исходное число 3 в число 300 и содержат не более пяти команд умножения?
'''
def f(x, y, k):
    if x > y:
        return 0
    if x == y:
        return 1
    if k < 5:
        return f(x + 1, y, k) + f(x * 3, y, k + 1) + f(x * 4, y, k + 1)
    else:
        return f(x + 3, y, k)

print(f(3, 300, 0))