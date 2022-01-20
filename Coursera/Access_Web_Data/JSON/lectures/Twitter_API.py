import urllib.request, urllib.parse, urllib.error
import json
from twurl import augment
import ssl

# https://apps.twitter.com/
# Creat app and get the four strings, put them in hidden.py

print('* Calling Twitter...')

url = augment('https://api.twitter.com/1.1/statuses/usre_timeline.json',
            {'screen_name': 'WeAre', 'count': '01' })

print(url)


# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#connection = urllib.request.urlopen(url, context=ctx)
#data = connection.read()
#print(data)

#headers = dict(connection.getheaders())
#print(headers)
