# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change_s(my_str: str) -> str:
    """ Описание функции """
    if my_str[-1] == 's' and  len(my_str) > 1:
        temp = my_str[0:-1]
        # print(temp)
        my_str = None
        return my_str, temp
    return my_str


a1 = 'seasons'
a2 = 'tables'
a3 = 'stat'
a4 = 'thunder'
a5 = 'laptops'

print(change_s(a1))

