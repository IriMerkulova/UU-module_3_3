#  "Распаковка"
#1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(f'{a}, {b}, {c}')


print_params()
print_params(2, 5)  # распаковка с двумя элементами
print_params('go')  # распаковка с одним элементом
print_params(b=25)  # 9 b 10 строки - распаковка с именованным элементом
print_params(c=[1, 2, 3])

#2. Распаковка параметров
values_list = [52, 'Hi', True]
values_dict = {'a': 35, 'b': 'start', 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3. Распаковка + отдельные параметры
values_list_2 = [2, 3.14]
print_params(*values_list_2, 42)
