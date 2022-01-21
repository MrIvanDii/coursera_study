class Car:
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999


#создадим объект класса Car и попытаемся получить доступ к переменной name. Выполним следующий скрипт:

car_a = Car()

print(car_a.name)
# Двигатель заведен
# corolla

#попробуем вывести значение переменной make. Выполняем следующий скрипт:

#print(car_a.make)
#AttributeError: 'Car' object has no attribute 'make'

