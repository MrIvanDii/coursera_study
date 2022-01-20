hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    pay = (((h - 40) * r) * 1.5) + (40 * 10.5)
else:
    pay = h * r

print(pay)
