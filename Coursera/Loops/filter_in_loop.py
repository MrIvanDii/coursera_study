#переменная для удобства
argument = [9, 41, 12, 3, 74, 15]



#создаем цикл который фильтрует данные по заданной
#инструкции и показателям (вывести все что > 20)
print('Before')
for value in argument:
    if value > 20:
        print ('Large number', value)
print('After')


#фильтрация данных используя BOOLean - если результат
#соответствует инструкции значит - все последующие
#результаты будут True, до этого все будет False
found = False
print('Before', found)
for value in argument:
    if value == 3:
        found = True
    print(found, value)
print('After', found)


#поиск наименьшего числа в списке данных используя
#функцию и наименьший показатель(точка отсчета)
#начинается с NONE
smallest = None
print('Before')
for value in argument:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
