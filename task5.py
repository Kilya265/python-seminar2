# Реализуйте алгоритм перемешивания списка.

import random

list = [random.randrange(10, 100) for i in range(int(input('Введите кол-во элементов списка: ')))]
list.sort()
print('Список до перемешивания: ', list)
random.shuffle(list)
print('Список после перемешивания: ', list)