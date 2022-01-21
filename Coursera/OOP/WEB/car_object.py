# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "c200"
    make = "mercedez"
    model = 2008

    # создаем методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


# Создаем объект класса Car под названием car_a
car_a = Car()

# Создаем объект класса Car под названием car_b
car_b = Car()

print(type(car_b))
#<class '__main__.Car'>

car_b.start()  # Вызов метода (действия) не требует команды print() или return, просто
# Заводим двигатель

print(car_b.model)  # Получения доступа к атрибуту происходит через команду print()
# 2008

print(dir(car_b))  # все атрибуты и методы объекта car_b
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'make', 'model', 'name', 'start', 'stop']

# обрати внимание на последние 5 строк списка : 'make', 'model', 'name', 'start', 'stop'
# эти строки - это наши атрибуты и методы объекта car_b

