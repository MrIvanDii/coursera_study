from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import requests


link = "http://py4e-data.dr-chuck.net/known_by_Carey.html"

count = 0
repeats =  7
names = []

while count < repeats:

    responce = requests.get(link).text

    url = re.findall('http://.*html', str(responce))
    name = re.findall('_.*_(.*)\.html', str(responce))

    names.append(name[17])

    link = url[17]

    count = count + 1
    #print(count)

#third_url = url[2]
    #print(link)
#print(url[1])
#print(names)
    #print(link)

print(names[6])
