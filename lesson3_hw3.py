"""
функциz my_func(), принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(a, b, c):
    L = [a, b, c]
    L.pop(L.index(min(L)))
    return (L[0] + L[1])
# example
print(my_func(78, 89, 96))