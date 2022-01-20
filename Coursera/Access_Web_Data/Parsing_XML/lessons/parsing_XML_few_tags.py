import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuk</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Atribute', item.get("x"))
#User count: 2
#Name Chuk
#Id 001
#Atribute 2
#Name Brent
#Id 009
#Atribute 7
