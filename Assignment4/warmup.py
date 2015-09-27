__author__ = 'Mac'

# Fahrenheit to celcius

# input for farenheit
input_fahrenheit = input('Give ur Fahrenheit input ')
# formula Fahrenheit to celcius
celcius = (input_fahrenheit - 32) * 5/9
# round celcius
celcius = round(celcius, 2)
# print celcius on screen
print 'celcius is: ',celcius

# celcius to kelvin




# input for celcius
input_celcius = input('Give ur Celcius input ')
while input_celcius < -273.15:
    input_celcius = input('Give a correct Celcius input ')

# formula Fahrenheit to celcius
kelvin = input_celcius + 273.15

# print kelvin on screen
print 'Kelvin is: ',kelvin






# absolute number
input_absnumber = input('Give ur absolute number ')

# build in function
absolute = abs(input_absnumber)


# check if number is below 0
if input_absnumber < 0:
    # flips number
    input_absnumber = -input_absnumber
else:
    input_absnumber = input_absnumber

print 'self, Your absolute number is: ',input_absnumber

# using a build in function
print 'build in, Your absolute number is: ',absolute




