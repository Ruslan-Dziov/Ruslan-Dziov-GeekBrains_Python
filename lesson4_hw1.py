from sys import argv
script_name, worked_out, cost_of_hour, bonus = argv


print('Название скрипта - ', script_name)
print('Выработка в часах - ', worked_out)
print('Ставка в час - ', cost_of_hour)
print('Премия - ', bonus)


def salary(worked_out, cost_of_hour, bonus):
    return (int(worked_out) * int(cost_of_hour)) + int(bonus)


sal = salary(worked_out, cost_of_hour, bonus)


print(f'Зарплата сотрудника составляет {sal} рублей')