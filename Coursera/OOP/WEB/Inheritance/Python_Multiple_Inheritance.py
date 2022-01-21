# Множественное наследование Python
# В Python, родительский класс может иметь несколько дочерних, и, аналогично,
# дочерний класс может иметь несколько родительских классов.
# Давайте рассмотрим первый сценарий. Выполним следующий скрипт:

# создаем класс Vehicle
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# создаем класс Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это дочерний метод из класса Car")


# создаем класс Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")


# В этом скрипте, родительский класс Vehicle наследуется двумя дочерними классами — Car и Cycle.
# Оба дочерних класса будут иметь доступ к vehicle_method() родительского класса.
# Запустите следующий скрипт, чтобы увидеть это лично:

car_a = Car()
car_a.vehicle_method() # вызов метода родительского класса
car_b = Cycle()
car_b.vehicle_method() # вызов метода родительского класса

# Это родительский метод из класса Vehicle
# Это родительский метод из класса Vehicle



# Вы можете видеть, как родительский класс наследуется двумя дочерними классами.
# Таким же образом, дочерний класс может иметь несколько родительских. Посмотрим на пример:

class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")


class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")



cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()

# Это родительский метод из класса Camera
# Это родительский метод из класса Radio

