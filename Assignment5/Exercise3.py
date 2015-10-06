__author__ = 'Mac'


string_input = raw_input('write a sentence ')
shift = input('enter a int ')

new_string = ''
begin = 0
temp = 0


for i in string_input:
    if i.isalpha():
        if i.isupper():
            begin = 65
        else:
            begin = 97
        temp = ord(i)

        shift %= 26

        temp = temp - begin + shift

        if temp < 0:
            temp += 26
        if temp >= 26:
            temp -= 26
        else:
            temp = temp

        temp += begin
        new_string += chr(temp)
    else:
        new_string += i

print new_string





