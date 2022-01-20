fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    #print(line)
    #if not line.startswith('From '): continue
    if line.startswith('From '):
        words = line.split()
        #print(words)
        print('#' + words[2])
#Sat
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Fri
#Thu
#Thu
#Thu
#Thu
#Thu
#Thu
