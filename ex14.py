user_integer = int(input('Please enter your integer: '))
while user_integer > 9:
    multy = 1
    for i in str(user_integer):
        multy = multy * int(i)
        print(multy)
        user_integer = multy
print(user_integer)
