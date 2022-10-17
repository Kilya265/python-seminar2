# Задайте список из n чисел последовательности (1+1/n)^n 
# выведите на экран их сумму.

n = int(input('Введите N: '))
def posled(n):
    return (1 + (1/n))**n

result = [posled(i) for i in range(1, n + 1)]
print('Сумма: ', round(sum(result), 3))
