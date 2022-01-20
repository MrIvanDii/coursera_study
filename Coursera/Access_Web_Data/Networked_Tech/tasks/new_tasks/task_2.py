from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


site = input('Enter site - ')
pos = 18
count = 7

html = urlopen(site).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

loop_count = 0


while loop_count < count:

    name=[]
    links=[]

    for tag in tags:

        decode_line = tag.decode()

        url = re.findall('href="(\S+?)"',decode_line)
        #url = re.findall('http://.*html',decode_line)

        #print(link)
        links.append(url)

        word = re.findall('>(\S+?)<',decode_line)
        #word = re.findall('_.*_(.*)\.html', decode_line)

        name.append(word)
        #print(name)

    flink = links[pos-1]

    for link in flink:

        html = urlopen(link).read()
        soup = BeautifulSoup(html, "html.parser")

        tags = soup('a')
        #print('Retrieving ; ',link)
        #print(url)
        #print(links)
        #print(name)
    #print(flink)
    loop_count = loop_count + 1

fname = name[pos-1]

print(fname)
