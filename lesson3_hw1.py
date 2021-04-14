def devision1():
    """
    ввод аргументов через input
    """
    x = float(input('Введите делимое '))
    y = float(input('ведите делитель '))
    if y == 0:
        print('На ноль делить нельзя!')
        return ('На ноль делить нельзя!')
    print(x / y)
    return (x / y)

devision1()

def devision2(x, y):
    """
    Ввод аргументов в скобки функции, если делитель = 0, функция запрашивает новый делитель.
    """
    if y == 0:
        print('На ноль делить нельзя!')
        return ('На ноль делить нельзя!')
    print(x / y)
    return (x / y)

devision2(2, 0)