# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


a = int(input())
sum = 0
print(a, end='')
while a > 0:
    i = a % 10
    sum = sum + i
    a = a // 10
print (f"-> {sum}")