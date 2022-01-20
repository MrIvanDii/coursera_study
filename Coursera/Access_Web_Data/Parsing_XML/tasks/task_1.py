import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
import urllib
import requests
import re


data = 'http://py4e-data.dr-chuck.net/comments_1417661.xml'
responce = requests.get(data).text

resp_str = str(responce)

tree = ET.fromstring(resp_str)

COMMENTS = tree.findall('.//comment')

numbers = []

for item in COMMENTS:
    num = item.find('count').text
    numbers.append(int(num))


print('User comments:', len(COMMENTS))
print('Sum of the numbers in the file:', sum(numbers))
