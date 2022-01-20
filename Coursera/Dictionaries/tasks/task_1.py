 #Write a program to read through the mbox-short.txt
 #and figure out who has sent the greatest number of mail messages.
 #The program looks for 'From ' lines
 #and takes the second word of those lines as the person who sent the mail.
 #The program creates a Python dictionary
 #that maps the sender's mail address to a count of the number of times
 #they appear in the file. After the dictionary is produced,
 #the program reads through the dictionary using a maximum loop
 #to find the most prolific committer.

fname = input("Enter file name: ")
 #запрашиваем у пользователя имя файла

fh = open(fname)
 #определяем переменную, которая открывает файл

data = []
 #определяем переменную в которую будем собирать данные

list_adress = []

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
    list_adress.append(i[1])
#print(list_adress)

counts = {}

for name in list_adress:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1


bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count


print(bigword, bigcount)
