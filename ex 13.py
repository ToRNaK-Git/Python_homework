import string
str = string.ascii_letters
user_string = input(' Please enter two letters separated by a hyphen: ')
letter1 = user_string[0]
letter2 = user_string[-1]
index1 = str.index(letter1)
index2 = str.index(letter2)
result = str[index1:index2+1]
print(result)








