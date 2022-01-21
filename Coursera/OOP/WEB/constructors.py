class Car:
    # создание атрибутов класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)

# В скрипте выше мы создали класс Car с одним атрибутом класса car_count.
# Класс содержит конструктор, который увеличивает значение car_count и выводит итоговое значение на экран.

car_a = Car()
car_b = Car()
car_c = Car()
#1
#2
#3

car_a = Car()
#4
