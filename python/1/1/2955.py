# Задача №2955. Улитка
#
# Улитка ползёт по вертикальному шесту высотой h метров,
# поднимаясь за день на a метров, а за ночь спускаясь на b метров.
# На какой день улитка доползёт до вершины шеста?
#
# Входные данные
# Программа получает на вход натуральные числа h, a, b. Гарантируется, что a>b.
#
# Выходные данные
# Программа должна вывести одно натуральное число.
#
# Примечание
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#
# Примеры
# входные данные
# 10
# 3
# 2
# выходные данные
# 8
# входные данные
# 20
# 7
# 3
# выходные данные
# 5

h = int(input())
a = int(input())
b = int(input())

print((h - a) // (a - b) + 1 + 1 % ((h - a) % (a - b) + 1))
