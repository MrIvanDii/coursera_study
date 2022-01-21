import urllib.request, urllib.parse, urllib.error
#import urlopen
import ssl
from bs4 import BeautifulSoup
#import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

site = input('Enter site - ')
count = 7
pos = 18


for i in range(count):
    #print(i)

    #html = urlopen(site).read()
    html = urllib.request.urlopen(site, context=ctx).read()

    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    loop_count = 0

    for tag in tags:
        #print(tag)
        loop_count = loop_count +1

        #stopping at desired position
        if loop_count > pos:
            break

        site = tag.get('href', None)

        name = tag.contents[0]

print(name)
