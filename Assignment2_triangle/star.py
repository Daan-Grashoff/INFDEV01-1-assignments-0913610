__author__ = 'Mac'

number = input('type a number ')

print "[+] pyramid \n"

for i in range(1, number):
    pyra = ""
    for j in range(number - i):
        pyra += "    "
    for j in range(1, i):
        pyra += "*   "
    for j in range(i, 0, -1):
        pyra += "*   "

    print pyra

print "\n [+] star \n"


for i in range(1, number):
    star = ""
    for j in range(number - i):
        star += "    "
    for j in range(1, i):
        star += "*   "
    for j in range(i, 0, -1):
        star += "*   "
    print star

for i in range(0, number):
    star = ""
    for j in range(0, i):
        star += "    "
    for j in range(0, number - i - 1):
        star += "*   "
    for j in range(number, i, -1):
        star += "*   "


    print star
