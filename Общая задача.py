#Тимушкин Сергей Владимирович, 3, J, Общая задача
'''
Определите класс A, включающий:
строку документирования класса 'Класс A';
метод set_a() для установки значения атрибута a;
метод get_a() для получения значения этого атрибута.

Определите класс B, включающий:
строку документирования класса 'Класс B';
конструктор, инициализирующий атрибут данных b создаваемых экземпляров;
метод get_b() для получения значения этого атрибута.

Определите класс C, наследующий классы A (задача №2) и B (задача №3) и включающий:
строку документирования класса 'Класс C = A + B';
конструктор, инициализирующий дополнительно атрибуты данных a и c создаваемых экземпляров;
собственные методы set_b() и set_c() для установки значений соответствующих атрибутов;
собственный метод get_c() для получения значения атрибута c

Определите класс D, включающий:
статический метод stat_print_dict, выводящий на экран словарь атрибутов переданного ему объекта класса;
метод класса cls_print_dict, выводящий на экран словарь атрибутов своего класса.
'''

class A:
    '''Класс A'''
    def set_a(self, a):
        self.a = a
    def get_a(self):
        return self.a

class B:
    '''Класс B'''
    def __init__(self, b):
        self.b = b
    def get_b(self):
        return self.b

class C(A, B):
    '''Класс C = A + B'''
    def __init__(self, a, c):
        self.a = a
        self.c = c
    def set_b(self, b):
        self.b = b
    def set_c(self, c):
        self.c = c
    def get_c(self):
        return self.c

class D():
    @staticmethod
    def stat_print_dict(obj):
            print(obj.__dict__)
    def cls_print_dict(self):
            print(self.__dict__)
