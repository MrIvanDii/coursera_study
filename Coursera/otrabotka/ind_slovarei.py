D = {'a': 1, 'b': 2, 'c': 3}

#print(D['d'])
#KeyError: 'd'

D['d'] = 'spam' #присваивание по несуществующему ключу 'd'

print(D)
#{'a': 1, 'b': 2, 'c': 3, 'd': 'spam'}
