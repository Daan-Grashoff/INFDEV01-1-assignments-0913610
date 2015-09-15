__author__ = 'Mac'

number = input('type a number ')

for i in range(0, number):
    if i != number-1:
        print '*' * ((number-1)-i) + ' ' * int(i) + '*'
    else:
        print '*' * number

print number