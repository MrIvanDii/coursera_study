import urllib.request
import urllib.parse
import urllib.error

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print(x)
