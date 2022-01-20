import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^X-DSPAM.*:', line):
        print('#' + line)
#X-DSPAM-Result: Innocent
#X-DSPAM-Processed: Sat Jan  5 09:14:16 2008
#X-DSPAM-Confidence: 0.8475
#X-DSPAM-Probability: 0.0000
#X-DSPAM-Result: Innocent
#X-DSPAM-Processed: Fri Jan  4 18:10:48 2008
#...
#...
