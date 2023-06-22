#Тимушкин Сергей Владимирович, 3, Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением.

def to_dict(lst):
    output_dict = dict()
    for elem in lst:
        output_dict[elem] = elem
    return output_dict

print(to_dict([1,2,3]))