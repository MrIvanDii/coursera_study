purse = {}
#определение словаря

purse['money'] = 12
#ключ = 'money' ; данные = 12

purse['candy'] = 3
#ключ = 'candy' ; данные = 3

purse['tissues'] = 75
#ключ = 'tissues' ; данные = 75
#добавление данных в существующий словарь

print(purse)
#{'money': 12, 'candy': 3, 'tissues': 75}

print(purse['candy'])
#3

purse['candy'] = purse['candy'] + 2
print(purse)
#{'money': 12, 'candy': 5, 'tissues': 75}
