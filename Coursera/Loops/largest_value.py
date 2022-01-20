#печатаем Before перед циклом
#запускаем цикл
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

#создаем цикл определяющий самое большое значение
#создаем начальную переменную, -
# - которая будет "точкой отсчета"
#указываем объяснение от чего начинаем
#создаем цикл поиска большего значения
#выводим значение на экран
largest_so_far = -1
print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
