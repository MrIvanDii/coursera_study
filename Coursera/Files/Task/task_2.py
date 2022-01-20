#Write a program that prompts for a file name,
#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.


fname = input("Enter file name: ")
#запрашиваем у пользователя имя файла

fh = open(fname)
#определяем переменную, которая открывает файл

list = []
#определяем перемнную-список, в которую будем добавлять данные

for line in fh:
#перебираем построчно данные в переменной fh

    if line.startswith("X-DSPAM-Confidence:"):
#условие: если строка начинается с 'X-DSPAM-Confidence:'

        list.append(line)
#добавить данные соответствующие условию - переменную list

list_num = []
#определяем новую переменную-список

for i in list:
#перебираем построчно данные в переменной list

    atposs = i.find('0')
#находим первую цифру "0" в строке i и ее индекс в этой троке

    number = i[atposs:len(i)]
#определяем переменную с координатами в строке - вырезаем кусок информации

    number = number.rstrip()
#убираем лишние пробелы(и окночания строки) используя метод .rstrip()

    list_num.append(number)
#в переменную list_num добавляем обработанные данные



count = 0
#определяю счетчик

result_of_num = 0.0
#определяю переменную с нулевыми данными - буду прибавлять к ней другие данные

while count < len(list_num):
#запускаю цикл

    for i in list_num:
#перебираю построчно данные в переменной list_num

        count = count + 1
#счетчик выполняет подсчет циклов

        result_of_num = result_of_num + float(i)
#добавляю в переменную нужные данные

    print('Average spam confidence:',result_of_num / len(list_num))
#вывод данных с средни показателем
