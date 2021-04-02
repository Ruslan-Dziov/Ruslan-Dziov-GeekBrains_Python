#Home work
#1
print('Home work #1')
integer = int(input("Введите челое число: "))
flt = float(input("Введите число с плавающей запятой: "))
string = str(input('Введите строку: '))
print('-> челое число ', integer)
print('-> число с плавающей запятой ', flt)
print('-> строка ', string)
print('\n', ' * ' * 30, '\n')

#2
print('Home work #2')
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'Введенное время в формате чч.мм.сс: %02d:%02d:%02d' % (hours, minutes, seconds))
print('\n', ' * ' * 30, '\n')

#3
print('Home work #3')
number = input('Введите число: ')
print(number, ' + ', number * 2, ' + ', number * 3, ' = ', int(number) + int(number * 2) + int(number * 3))
print('\n', ' * ' * 30, '\n')

#4
print('Home work #4')
number4 = input('Введите число: ')
max_figure = int(number4[0])
i = 0
while i < len(number4):
    interim = int(number4[i])
    if interim > max_figure:
        max_figure = interim
    i += 1
print('Максимальная цифра в введенном числе: ', max_figure)
print('\n', ' * ' * 30, '\n')

#5
print('Home work #5')
revenues = int(input('Введите сумму выручки: '))
expenses = int(input('Введите сумму издержек: '))
if revenues > expenses:
    print('Компания получила прибыль в размере: ', revenues - expenses, '$')
    print('Рентабельность составила ', (revenues - expenses) * 100 / revenues, '%')
    staff = int(input('Введите количество сотрудников компании '))
    print('Прибыль в расчете на одного сотрудника составляет ', (revenues - expenses) / staff, '$')
else:
    print('Компания понесла убытки в размере ', expenses - revenues, '$')
print('\n', ' * ' * 30, '\n')

#6
print('Home work #6')
a = int(input('Результат первого дня: '))
b = int(input('Требуемый дневной результат: '))
day = 1
print(f'{day}-й день: {a} км')
while a < b:
    a = round((1.1 * a), 2)
    day += 1
    print(f'{day}-й день: {a} км')
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')
