# Задача №2945. Следующее четное
# Дано целое число n. Выведите следующее за ним четное число.
# При решении этой задачи нельзя использовать условную инструкцию if и циклы.
# входные данные
# 7
# выходные данные
# 8
# входные данные
# 8
# выходные данные
# 10

n = int(input())
n += 2 - n % 2
print(n)
