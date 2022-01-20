
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

tags = soup('span')
#print(tags)
#for tag in tags:
all_numbers = []
numbers = re.findall('[0-9]+', str(tags))
#print(num)
for number in numbers:
    number = int(number)
    all_numbers.append(number)
print(sum(all_numbers))
    #data.append(num)
    #for char in tag:
        #if char in numbers:
            #data.append(char)
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print(data)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
