__author__ = 'Mac'

from math import sqrt

radius = input('give radius of circle (min 10) ')
face = raw_input('face? ')

circle = ''
circle2 = ''

mouth_length = 0


for x in range(1, radius):
    for y in range(radius):
        disx = x - radius/2
        disy = y - radius/2
        dist = sqrt((disx**2) + (disy**2))
        if dist < radius / 2 and dist > radius/2.6:
            circle2 += '*'
        elif face:
            if x == radius/2 and y == radius/2:
                circle2 += '#'
            elif (x == radius/3+1 and y == radius/3):
                circle2 += '-'
            elif (x == radius/3+1 and y == radius/3*2+1):
                circle2 += '-'
            elif (x == radius/3 and y == radius/3) or (x == radius/3 and y == radius/3*2+1):
                circle2 += '~'
            elif x == radius/4*3 and dist < radius / 3:
                circle2 += '_'
            else:
                circle2 += ' ';
        else:
            circle2 += ' ';
    circle2 += '\n'
print circle2

#
#
# for x in range(radius * 2):
#     for y in range(radius * 2):
#         if sqrt((radius - x)**2 + (radius - y)**2) < radius:
#             circle += '*'
#         else:
#             circle += ' '
#     circle += '\n'
#
#
# print circle