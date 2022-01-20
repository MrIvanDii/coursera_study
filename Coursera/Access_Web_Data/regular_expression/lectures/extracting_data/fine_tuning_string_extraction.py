import re

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+', x)

print(y)
#['stephen.marquard@uct.ac.za']




z = re.findall('^From (\S+@\S+)', x)

print(z)
#['stephen.marquard@uct.ac.za']


#скобки во втором примере (\S+@\S+) - не являются частью обозначения того что
#надо извлечь. Но они они обозначают начало и конец части которую нужно извлечь.
