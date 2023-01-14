'''
Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу. Найдите все
натуральные числа, принадлежащие отрезку [1523467; 4157812] и имеющие ровно три нетривиальных делителя.
Для каждого найденного числа запишите в ответе два числа: само число и его наибольший нетривиальный делитель.
Найденные числа расположите в порядке возрастания.
'''
def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


for q4 in range(round((1523467**0.25)), round((4157812**0.25)) + 1):
    x = q4 ** 4
    if 1523467 <= x <= 4157812 and prost(q4):
        print(x, max([q4, q4**2, q4**3]))


