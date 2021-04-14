"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce
my_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(pr_el, el):
    return pr_el * el


result = reduce(my_func, my_list)

#print(my_list)
print(result)