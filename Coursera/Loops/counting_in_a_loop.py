#переменная для удобства
argument = [9, 41, 12, 3, 74, 15]

#создаем цикл
#считающий колличество выполненных итераций
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)



#создаем цикл который сумирует все данные аргумента
#и в конце выводит сумму всех аргументов
zork = 0
print('Before', zork)
for thing in argument:
    zork = zork + thing
    print(zork, thing)
print('After', zork)



#создаем цикл который посчитает колличество:
#итераций, сумму аргументов, разделит одно на другое и
#выведет результаты всех процессов

count = 0
sum = 0
print('Before', count, sum)
for value in argument:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
