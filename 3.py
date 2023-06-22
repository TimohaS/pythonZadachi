#Тимушкин Сергей Владимирович, 3, Декоратор замедляющий время выполнения функции

from time import sleep

def frozen(input_func):
    def is_int(str):
        try:
            int(str)
            return True
        except ValueError:
            return False
    def output_func():
        print("Введите количество секунд для замедления функции")
        n = 0
        check = True
        while check:
            n = input()
            if is_int(n):
                n = int(n)
                if n < 0:
                    print("Количество секунд должно быть положительным числом")
                else:
                    check = False
            else:
                print("Количество секунд должно быть целым числом")
        sleep(n)
        input_func()
    return output_func

@frozen
def hello():
    print("Hello World")

hello()