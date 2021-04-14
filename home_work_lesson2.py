#1.
print('\n Задание 1 - Типы данных в списке \n')
list_a = ['месяц', 7, True, (77, 88, 99), 112.3]
print(list_a, '\n')
for i in list_a:
    print(type(i))
print('\n', ' * ' * 30,'\n')

#2.
print('\n Задание 2 - обмен значений соседних элементов списка\n')
#Ввод данных
list_b = []
list_el = None
while True:
    list_el = input('Введите элемент списка, или нажмите ввод чтобы продолжить  ')
    if list_el == '':
        break
    list_b.append(list_el)
if list_b == []:
    print('К сожалению список пуст, мы не можем продолжать')
#обмен значений соседних элементов
i = 0
while (i + 1) < len(list_b):
    list_b[i], list_b[(i + 1)] = list_b[(i + 1)], list_b[i]
    i += 2
print(list_b)
print('\n', ' * ' * 30,'\n')

#3.
print('\n Задание 3 - определение времени года по номеру месяца \n')
month = int(input('ведите номер месяца (определяем через список) '))
list_year = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month in list_year[0:3]:
    print('Это зима')
elif month in list_year[3:6]:
    print('Это весна')
elif month in list_year[6:9]:
    print('Это лето')
elif month in list_year[9:11]:
    print('Это осень')
else:
    print('Такого месяца не существует')
#через dict
month_d = int(input('ведите номер месяца (определяем через словарь) '))
dict_year = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень'}
if month_d in dict_year.keys():
    print('Это', dict_year.get(month_d))
else:
    print('Такого месяца не существует')
print('\n', ' * ' * 30,'\n')

#4.
print('\n Задание 4 - вывести нумерованный список слов введенных через пробел \n')
string_4 = input('Введите строку из нескольких слов: ')
list_str4 = string_4.split()
for numb, str4 in enumerate(list_str4, 1):
    print(numb, str4[0:10])
print('\n', ' * ' * 30,'\n')

#5.
print('\n Задание 5 - структура "Рейтинг" \n')
my_list = [7, 5, 3, 3, 2]
while True:
    new_num = input('Добавьте число в рейтинг или нажмите "Enter" чтобы выйти ')
    if new_num == '':
        break
    new_num = int(new_num)
    my_list.append(new_num)
    my_list.sort()
    my_list.reverse()
    print(my_list)
print('\n', ' * ' * 30,'\n')

#6.
print('\n Задание 6 - Структура данных "Товары" \n')
list_cat = []
counter = 0
while True:
    add_position = input('\nВвести позицию? ("Enter" - да, N - нет) ')
    if add_position == 'N':
        break
    dict_cat = {}
    key_name = 'название'
    value_name = input('введите название ')
    name = {key_name: value_name}
    dict_cat.update(name)
    key_price = 'цена'
    value_price = input('Введите цену ')
    #Защита от инициативных пользователей :) цена либо int либо float если с копейками
    while True:
        if value_price.isdigit():
            break
        if '.' in value_price:
            split_price = value_price.split('.')
            if len(split_price) == 2 and split_price[0].isdigit() and split_price[1].isdigit():
                break
        print('Цена должна состоять из цифр и точки')
        value_price = input('Введите цену ')
    value_price = float(value_price)
    price = {key_price: value_price}
    dict_cat.update(price)
    key_qty = 'количество'
    value_qty = input('Введите количество ')
    # Защита от инициативных пользователей :) количество товара - int, хотя наверно может быть и float
    while True:
        if value_qty.isdigit():
            break
        print('Количество должно состоять из цифр')
        value_qty = input('Введите количество ')
    value_qty = int(value_qty)
    qty = {key_qty: value_qty}
    dict_cat.update(qty)
    key_unit = 'ед.'
    value_unit = (input('Введите единицу измерения '))
    unit = {key_unit: value_unit}
    dict_cat.update(unit)
    counter += 1
    tuple_cat = (counter, dict_cat)
    list_cat.append(tuple_cat)
print('\n', 'структура данных: \n', list_cat)
#делаем аналитику товаров, как в примере задания
names_list = []
prices_list = []
qty_list = []
units_list = []
for items in list_cat:
    dict_position = items[1]
    names_to_list = dict_position.get(key_name)
    names_list.append(names_to_list)
    prices_to_list = dict_position.get(key_price)
    prices_list.append(prices_to_list)
    qty_to_list = dict_position.get(key_qty)
    qty_list.append(qty_to_list)
    unit_to_list = dict_position.get(key_unit)
    units_list.append(unit_to_list)
dict_analytics = {
    key_name: names_list,
    key_price: prices_list,
    key_qty: qty_list,
    key_unit: units_list
}
print('\n Аналитика товаров: \n', dict_analytics)
#если надо исключить повторяющиеся пункты в списках значений словаря, по примеру решения я подумал, что надо удалить повторения, пишу на всякий случай
dict_analytics = {
    key_name: list(set(names_list)),
    key_price: list(set(prices_list)),
    key_qty: list(set(qty_list)),
    key_unit: list(set(units_list))
}
print('\n Исключаем повторения значений: \n', dict_analytics)