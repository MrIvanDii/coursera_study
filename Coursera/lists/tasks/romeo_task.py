#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list
#and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
#запрашиваем у пользователя имя файла

fh = open(fname)
#определяем переменную, которая открывает файл

inp = fh.read()
#определяем переменную которая содержит весь прочитанный текст

lst = inp.split()
#определяем переменную которая принимает данные из переменной inp, разделяет их
#и создает список

new_lst = []
#определяем перемнную-список, в которую будем добавлять данные

for i in lst:
#перебираем построчно данные в переменной lst
    if i not in new_lst:
#условие: если данные не находятся в списке new_lst - выполняем следующую инструкцию

        new_lst.append(i)
#добавить в переменную new_lst данные соответствующие условию выше

        new_lst.sort()
#сортируем данные внутри списка (по умолчание сортировка происходит в алфавитном порядке)

print(new_lst)
#выводим список на экран
