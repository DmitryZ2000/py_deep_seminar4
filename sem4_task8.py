# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change_dic(my_dict: dict) -> dict:
    """ Описание функции """
    temp_dict = {}
    for key, value in my_dict.items():        
        if key[-1] == 's' and  len(key) > 1:
            my_dict[key] = None
            temp_dict[key[0:-1]] = value 
        my_dict = my_dict | temp_dict
    return my_dict

seasons = 5
tables = 9
state = 25
thunder = 100
laptops = 200

global_dict = {key: value for key, value in globals().items() if not key.startswith('__')}
# global_dict_2 = dict(filter(lambda x: not x[0].startswith('__'),globals().items()))
# print(global_dict2)
print(globals())
print(global_dict)
print(change_dic(global_dict))

