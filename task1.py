# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

n = float(input("Введите число: "))

def sum(n):
    if n < 0:
        x = n * (-1)
    number = 0

    for i in str(n):
        if i != '.':
            number += int(i)
    return number

print(f'Сумма: {sum(n)}')
