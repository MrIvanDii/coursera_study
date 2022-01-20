fhand = open('romeo.txt')

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(sorted( [ (v,k) for k,v in counts.items() ] ) )

#[(1, 'Arise'), (1, 'But'), (1, 'It'), (1, 'Juliet'), (1, 'Who'),
#(1, 'already'), (1, 'breaks'), (1, 'east'), (1, 'envious'), (1, 'fair'),
#(1, 'grief'), (1, 'kill'), (1, 'light'), (1, 'moon'), (1, 'pale'),
#(1, 'sick'), (1, 'soft'), (1, 'through'), (1, 'what'), (1, 'window'),
#(1, 'with'), (1, 'yonder'), (2, 'sun'), (3, 'and'), (3, 'is'), (3, 'the')]

a = []

b = ()

print(dir(a))
print(dir(b))

x , y = 3, 4

print(y)

data = [1, 5, 2, 9, 11, 8, 4]
data.sort(reverse=True)
print(data)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
