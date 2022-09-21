from math import tan, radians
count = 0
k = tan(radians(90))  # tg угла 30 градусов
for x in range(1, 201):
  for y in range(1, 201):
    if y < -k * x + 50 and y > k * x:
      count += 1
print(count)
