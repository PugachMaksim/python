# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

N = int(input())
mas = []
for i in range (N):
    mas.append(randint(0, 5))
print(mas)
X = int(input())
sum = 0
for j in range (len(mas)):
    if mas[j] == X:
        sum += 1
print(f"число {X} встречается {sum} раз")