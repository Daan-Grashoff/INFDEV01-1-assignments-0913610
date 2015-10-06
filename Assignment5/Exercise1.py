__author__ = 'Mac'

input = raw_input('input some text ')


array = []
for i in input:
    array.append(i)

# or use list(input)


newstring = ''
for i in range(0, len(array)):
    newstring += array.pop(-1)

print newstring

