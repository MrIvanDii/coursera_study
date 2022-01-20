d = {'a':10, 'b':1, 'c':22}

t = sorted(d.items())

print(t)
#[('a', 10), ('b', 1), ('c', 22)]

for k,v in t:
    print(k,v)

#a 10
#b 1
#c 22
