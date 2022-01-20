line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = line.split()

print(words)
#['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

email = words[1]

print(email)
#stephen.marquard@uct.ac.za

pieces = email.split('@')

print(pieces[1])
#uct.ac.za


#THE REG EXPRESSION


import re

line_reg = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('@([^ ]*)', line_reg)

print(y)
#['uct.ac.za']


#[^ ]*
#[^ ] - подобрать один безпробельный символ, * - подобрать максимальное колличество
#безпробельных символов


line_reg = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

z = re.findall('@(\S*)', line_reg)

print(z)
#['uct.ac.za']

#(\S*)
#\S - подобрать один безпробельный символ, * - подобрать максимальное колличество
#безпробельных символов после символа "@"


#БОЛЕЕ ТОЧНАЯ НСТРОЙКА

line_reg = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

z = re.findall('^From .*@([^ ]*)', line_reg)

print(z)
#['uct.ac.za']


#.*@([^ ]*)

#В данном куске инструкции мы указываем что существует информация до символа "@"
# .*@   - но нас интересует другая информация, именно та
#что в круглых скобках  ([^ ]*)  - а имеено все безпробельные символы после
# символа "@"
