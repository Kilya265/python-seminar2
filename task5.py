# Реализуйте алгоритм перемешивания списка.

import random

list = [random.randrange(1, 100) for i in range(int(input('Введите кол-во элементов списка: ')))]
list.sort()
print('Список до перемешивания: ', list)
rand = random.sample(list, len(list))
print('Список после перемешивания: ', rand)
