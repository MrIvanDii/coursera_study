#Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

#fname = input("Enter file name: ")
 #запрашиваем у пользователя имя файла

fh = open('mbox-short.txt')
 #определяем переменную, которая открывает файл

data = []
 #определяем переменную в которую будем собирать данные

list_time = []

for line in fh:
 #перебираем построчно данные в файле
    if line.startswith('From '):
 #условие: когда строка начинается с 'From ' - делаем следующее
        data_1 = line.split()
 #переменная data_1 - принимает и разделяет данные которые соответствуют условию
        data.append(data_1)
 #в переменную data добавляем списки с данными data_1

#print(data)

for i in data:
#перебираем данные в списке data
    list_time.append(i[5].split(':'))


list_hours = []

for hours in list_time:
    list_hours.append(hours[0])

list_hours = sorted(list_hours, reverse=False)


count_hours = dict()

for count_h in list_hours:
    if count_h not in count_hours:
        count_hours[count_h] = 1
    else:
        count_hours[count_h] = count_hours[count_h] + 1

#count_hours = sorted(count_hours, reverse=False)
#print(list_time)
#print(list_hours)
#print(count_hours)

for key in count_hours:
    print(key, count_hours[key])
