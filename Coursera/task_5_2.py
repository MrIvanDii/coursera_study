#Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'. Once 'done' is entered,
#print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number
#catch it with a try/except and put out an appropriate message
#and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.


data = []

number = input('Pleas input your number:')

while number != 'done':
    try:
        num = int(number)
    except:
        pass
        exception = 'Invalid input'

    data.append(num)
    number = input('Pleas input your number:')

largest_num = -1

for the_num in data:
    if the_num > largest_num:
        largest_num = the_num

smallest = None

for value in data:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value


print(exception)
print('Maximum is ' + str(largest_num))
print('Minimum is ' + str(smallest))
