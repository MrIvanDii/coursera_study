from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#Importing libraries

site = input('Enter site - ')
pos = 18 #Taking input of position where to start from
count = 7 #Taking input of number of times to repeat

html = urlopen(site).read() #Opening and reading the webpage
soup = BeautifulSoup(html, "html.parser") #Making the html document easy to read
tags = soup('a') #Searching for all the anchor tags

loop_count = 0 #big count of running the program


while loop_count < count: #Checking the condition to run program till input count

    name=[] #Putting the name list blank to store names
    links=[] #Putting links list blank to store the anchor links

    for tag in tags: #Going through all the anchor tags

        decode_line = tag.decode() #Decoding the line to read it

        link = re.findall('href="(\S+?)"',decode_line) #Finding the link in the anchor tag using Regular Expressions

        #print(link)
        links.append(link) #Storing the link to access later

        word = re.findall('>(\S+?)<',decode_line) #Finding the name in the anchor tag

        name.append(word) #Storing the name to access later
        #print(name)

    flink = links[pos-1] #Retrieving the link which we need to go to

    for link1 in flink: #Flink becomes a list so we can't pass it through urllib so retrieving it as a string
        html=urlopen(link1).read() #Passing the webpage link as a string and opening it (Next webpage)
        soup = BeautifulSoup(html, "html.parser") #Making the html document easy to read (Next webpage)
        tags=soup('a') #Searching for all the anchor tags (Next webpage)
        #print('Retrieving ; ',link1)
        #print(link)
        #print(links)
        #print(name)
    #print(flink)
    loop_count = loop_count + 1

fname = name[pos-1]

print(fname)
