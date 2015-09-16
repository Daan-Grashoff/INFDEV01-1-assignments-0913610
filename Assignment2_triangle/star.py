__author__ = 'Mac'



try:
    number = input('type a number ')
except SyntaxError:
    number = 5

try:
    star_char = raw_input('star as ')
except SyntaxError:
    star_char = '*'

if star_char == '':
    star_char = "&&&"


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
    for j in range(-i, 0):
        star += "*   "
    print star

for i in range(0, number):
    star = ""
    for j in range(0, i):
        star += "    "
    for j in range(0, number - i - 1):
        star += "*   "
    for j in range(0, number - i):
        star += "*   "
    print star

print "\n [+] Custom star with custom char \n"


for i in range(1, number):
    star = ""
    for j in range(number - i):
        star += "  " + (' ' * int(len(star_char)-1))
    for j in range(1, i):
        star += "%s " % star_char
    for j in range(-i, 0):
        star += "%s " % star_char
    print star

for i in range(0, number):
    star = ""
    for j in range(0, i):
        star += "  " + (' ' * int(len(star_char)-1))
    for j in range(0, number - i - 1):
        star += "%s "  % star_char
    for j in range(0, number - i):
        star += "%s " % star_char
    print star
