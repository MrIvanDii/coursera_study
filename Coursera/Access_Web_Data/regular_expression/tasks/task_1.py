import re

hand = open('mbox-short.txt')

numlist = []

for line in hand:
    line = line.rstrip()
    numbers = re.findall('([0-9]+)', line)
    for i in numbers:
        i = int(i)
        numlist.append(i)

print(sum(numlist))
