import requests
import re

link = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = 0
repeats = 4
names = []

while count < repeats:

    responce = requests.get(link).text

    url = re.findall('http://.*html', str(responce))
    name = re.findall('_.*_(.*)\.html', str(responce))

    names.append(name[2])

    link = url[2]

    count = count + 1
    #print(count)

#third_url = url[2]
#print(url)
#print(url[1])
#print(name[1])
    #print(link)

print(names[3])
