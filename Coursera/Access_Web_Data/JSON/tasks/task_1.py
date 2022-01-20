import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
import urllib
import requests
import re
import json


data = 'http://py4e-data.dr-chuck.net/comments_1417662.json'
responce = requests.get(data).text
#print(responce)

#for i in responce:
    #print(i)


#resp_str = str(responce)
#print(resp_str)

info = json.loads(responce)
data = info['comments']
numbers = []

for i in data:
    nums = i['count']
    numbers.append(nums)

print(sum(numbers))


#print(data)

#print(len(info))

#numbers = []

#for item in info:
    #for item in comments:
        #print(item)
    #num = item.find('count').text
    #numbers.append(int(num))




#numbers = info['count']
#print(info['count'])
#print('Name:', info["name"])

#tree = ET.fromstring(resp_str)

#COMMENTS = tree.findall('.//count')

#print(COMMENTS)

#numbers = []

#for item in COMMENTS:
    #num = item.find('count').text
    #numbers.append(int(num))


#print('User comments:', len(COMMENTS))
#print('Sum of the numbers in the file:', sum(numbers))
