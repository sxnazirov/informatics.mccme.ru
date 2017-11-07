# Задача №2937. Следующее и предыдущее

# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере.
# Пробелы, знаки препинания, заглавные и строчные буквы важны!

# 179
# The next number for the number 179 is 180.
# The previous number for the number 179 is 178.

num = int(input())
print('The next number for the number %d is %d.' % (num, num + 1))
print('The previous number for the number %d is %d.' % (num, num - 1))
