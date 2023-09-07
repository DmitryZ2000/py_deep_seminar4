# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def dic_func(**kwarg):
    """ Функция создания словаря """
    my_dic = {}
    for key, value in kwarg.items():
        my_dic[key] = value
    return my_dic

print(dic_func(a=1, b=2, c=3, apple='iphone14'))