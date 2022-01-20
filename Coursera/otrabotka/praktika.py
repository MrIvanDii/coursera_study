a = 2 / 5
a_1 = 2 / 5.0
print(a, a_1)
#0.4
#0.4



b = "green %s and %s" % ("eggs", 'S')
print(b)
#green eggs and S



b_1 = 'green {0} and {1}'.format('eggs', 'S')
print(b_1)
#green eggs and S



c = ('x',)[0]
print(c)
#x

c_1 = ('x', 'y')[1]
print(c_1)
#y



L = [1,2,3] + [4,5,6]
print(L, L[:], L[:0], L[-2], L[-2:])
#[1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6] [] 5 [5, 6]



L_1 = ([1,2,3] + [4,5,6])[2:4]
print(L_1)
#[3, 4]
