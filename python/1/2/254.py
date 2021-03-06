# Задача №254. Ладья
#
# Требуется определить, бьет ли ладья, стоящая на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.
#
# Входные данные
# Вводятся четыре числа: координаты ладьи (два числа) и координаты другой фигуры (два числа),
# каждое число вводится в отдельной строке. Координаты - целые числа в интервале от 1 до 8.
#
# Выходные данные
# Требуется вывести слово YES, если ладья сможет побить фигуру за 1 ход и NO - в противном случае.
#
# Примеры
# входные данные
# 1
# 1
# 2
# 2
# выходные данные
# NO
# входные данные
# 1
# 1
# 2
# 1
# выходные данные
# YES

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
