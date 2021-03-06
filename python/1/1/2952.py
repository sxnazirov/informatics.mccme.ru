# Задача №2952. Разность времен
# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы,
# минуты и секунды для каждого из моментов времени.
# Известно, что второй момент времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.
#
# Входные данные
# Программа на вход получает три целых числа — часы, минуты, секунды, задающие первый момент времени и три целых числа,
# задающих второй момент времени.
#
# Выходные данные
# Выведите число секунд между этими моментами времени.
#
# Примеры
# входные данные
# 1
# 1
# 1
# 2
# 2
# 2
# выходные данные
# 3661
# входные данные
# 1
# 2
# 30
# 1
# 3
# 20
# выходные данные
# 50

# 1 - solution
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

print((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1)

# 2 - solution
s = 3600 * int(input())
s += 60 * int(input())
s += int(input())

s -= 3600 * int(input())
s -= 60 * int(input())
s -= int(input())

print((-1) * s)
