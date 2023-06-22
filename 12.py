#Тимушкин Сергей Владимирович, 3, Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел по возрастанию и возвращает его. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

def tpl_sort(tpl):
    if (''.join(map(str,tpl))).isdigit():
        tpl = list(tpl)
        for i in range(len(tpl) - 1):
            for k in range(len(tpl) - i - 1):
                if tpl[k] > tpl[k+1]:
                    tpl[k], tpl[k+1] = tpl[k+1], tpl[k]
        tpl = tuple(tpl)
    return tpl

print(tpl_sort((3,2,1)))
print(tpl_sort(('abc', '2', '1')))