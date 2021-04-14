"""
функция, принимает несколько параметров, как именованные аргументы, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Выводит данных о пользователе одной строкой.
"""

def user_data1(name, surname, age_of_birth, town, e_mail, phone):
    print(f"name - {name}; surname - {surname}; age_of_birth - {age_of_birth}; town - {town}; e_mail - {e_mail}; phone - {phone}")

user_data1('James', 'Bond', 1953, 'London', 'james.bond@yandex.ru', '+7 007 007 007')

print('\nВ словаре (**kwargs):')

def user_data2(**user_data):
    print(user_data)
user_data2(name = 'James', surname='Bond', age_of_birth=1953, town='London', e_mail='james.bond@yandex.ru', phone='+7 007 007 007')
