__author__ = 'Mac'
import math

input_number = input('number of square ')


print "A full square:"
square_string = ""
for i in range(0, input_number):
    for j in range(0, input_number):
        square_string += "*"
    square_string += '\n'

print square_string

print "A hollow square: "
hollowsquare_string = ""
for i in range(0, input_number):
    for j in range(0, input_number):
        if i == 0 or i == input_number-1:
            hollowsquare_string += "*"
        else:
            if j == 0 or j == input_number-1:
                 hollowsquare_string += "*"
            else:
                hollowsquare_string += " "
    hollowsquare_string += '\n'
print hollowsquare_string

print "A full rectangle triangle: "
fullrec_string = ""
for i in range(0, input_number):
    temp_number = i + 1
    for j in range(0, temp_number):
        fullrec_string += "*"
    fullrec_string += "\n"

print fullrec_string

print "A full isosceles triangle:"
isosrec_string = ""
for i in range(0, input_number):
    temp_number = (i * 2) + 1
    for ii in range(1, input_number - i):
        isosrec_string += " "
    for j in range(0, temp_number):
        isosrec_string += "*"
    isosrec_string += "\n"

print isosrec_string