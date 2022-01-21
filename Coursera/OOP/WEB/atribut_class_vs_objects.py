class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1



# создадим объект класса Car и вызовем метод start().

car_a = Car()
car_a.start("Corrola", "Toyota", 2015)

print(car_a.name)
print(car_a.car_count)

#Двигатель заведен
#Corrola
#1  ---   атрибут car_count


# создадим еще один объект класса Car и вызываем метод start().

car_b = Car()
car_b.start("City", "Honda", 2013)

print(car_b.name)
print(car_b.car_count)

#Двигатель заведен
#City
#2   ---   атрибут car_count увеличивается, потому что он атрибут класса а не объекта
