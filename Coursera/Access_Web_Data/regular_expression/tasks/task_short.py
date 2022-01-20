import re
print( sum( [ number.append(i) for i in re.findall('[0-9]+', hand.read('mbox-short.txt')) ] ) )
