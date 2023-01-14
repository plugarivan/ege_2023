'''
Среди целых чисел, принадлежащих числовому отрезку [412567; 473265], найдите числа, которые представляют собой
произведение двух различных простых делителей. Запишите в ответе количество таких чисел и то из них,
которое ближе всего к их среднему арифметическому.
'''
def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


ans = []
for i in range(412567, 473266):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d):
            ans.append(i)

sred = sum(ans) / len(ans)
diff = [abs(x-sred) for x in ans]
ind = diff.index(min(diff))

print(len(ans), ans[ind])
