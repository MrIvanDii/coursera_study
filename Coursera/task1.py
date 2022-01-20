def computepay():
    hours = input('Pleas enter your working hours:')
    rate = input('Pleas enter you working rate:')

    h = float(hours)
    r = float(rate)

    extra_time = 1.5

    if h > 40:
        pay = (((h - 40) * r) * extra_time) + (40 * r)
    else:
        pay = h * r

    return 'Pay ' + str(pay)

print(computepay())
