# Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

num = int(input('Введите N: '))
list = [random.randrange(-num, num + 1) for i in range(num)]
result = []
print('Заполненный список: ', list)

total = result.pop(0)
for i in result:
    total *= i
    print('Произведение элементов: ', total)

