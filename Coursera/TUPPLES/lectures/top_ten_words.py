fhand = open('romeo.txt')

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


lst = list()

for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)
#the 3
#is 3
#and 3
#sun 2
#yonder 1
#with 1
#window 1
#what 1
#through 1
#soft 1
