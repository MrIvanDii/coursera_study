fname = input('Enter the file name:')

fname = open(fname)
inp = fname.read()

inp = inp.rstrip()


print(inp.upper())
