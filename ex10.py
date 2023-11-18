import keyword
import string
user_string = input(' Please enter your variable :')
check = True
if user_string[0].isdigit():
    check = False
elif user_string in keyword.kwlist:
    check = False
elif not user_string.islower() and user_string != '_':
    check = False
else:
    for i in user_string:
        if i in string.punctuation and i != '_':
            check = False
            break
        elif i.isspace():
            check = False
            break
print(check)

