__author__ = 'Mac'

input = raw_input('input some text ')

countLowercase = 0
countCapitalcase = 0
countSpecialcase = 0
countNumber = 0
countEmpty = 0
allChars = 0

secureLevel = 0

diff =[
    'weak',
    'medium',
    'high'
]


# array = []
# for i in input:
#     array.append(i)

# or use list(input)


for i in input:
    allChars += 1
    if i.islower():
        countLowercase += 1
    elif i.isupper():
        countCapitalcase += 1
    elif i == ' ':
        countEmpty += 1
    elif i.isdigit():
        countNumber += 1
    else:
        countSpecialcase += 1

if countLowercase:
    secureLevel += 1

if countCapitalcase:
    secureLevel += 1

if countCapitalcase:
    secureLevel += 1

if countNumber:
    secureLevel += 1

for a in range(0, countEmpty):
    secureLevel += 1

if allChars < 6:
    secureLevel = 0
elif allChars > 10:
    secureLevel += 1


if secureLevel == 0:
    print "Not allowed"
elif secureLevel == 1:
    print "Weak"
elif secureLevel >= 2 and secureLevel <= 3:
    print "Medium"
elif secureLevel >= 4 and secureLevel <= 5:
    print "high"
elif secureLevel > 5:
    print "Secure"