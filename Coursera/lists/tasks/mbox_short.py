#Open the file mbox-short.txt and read it line by line. When you find a line that
#starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line
#(i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

fname = input("Enter file name: ")
#запрашиваем у пользователя имя файла

fh = open(fname)
#определяем переменную, которая открывает файл

data = []
#определяем переменную в которую будем собирать данные

for line in fh:
#перебираем построчно данные в файле
    if line.startswith('From '):
#условие: когда строка начинается с 'From ' - делаем следующее
        data_1 = line.split()
#переменная data_1 - принимает и разделяет данные которые соответствуют условию
        data.append(data_1)
#в переменную data добавляем списки с данными data_1

for i in data:
#перебираем данные в списке data
    print(i[1])
#выводим каждое значине из списка data с индексом i[1], тоесть каждое второе значение
print('There were', len(data), 'lines in the file with From as the first word')
#печатаем результат с колличеством строк в списке data - это наше колличество адресов
