class PartyAnimal:              # вызов класса PartyAnimal (создание класса)
    x = 0                       # атрибут класса


    def party(self):            # метод класса
        self.x = self.x + 1     # увеличение атрибута X
        print("So far", self.x)

an = PartyAnimal()              # инициализация объекта - an -     (создание объекта)


#--------------------------------------------------------------------------------------------------------



an.party()                      # вызов метода .party() объектом - an -
an.party()                      # вызов метода .party() объектом - an -
an.party()                      # вызов метода .party() объектом - an -

# So far 1
# So far 2
# So far 3

#---------------------------------------------------------------------------------------------------------

print("Type", type(an))                     # получаем информацию о том к какому типу относится переменная - an -
#Type <class '__main__.PartyAnimal'>

print("Dir", dir(an))                       # узнаем какие методы доступны переменной - an -

# Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'party', 'x']
