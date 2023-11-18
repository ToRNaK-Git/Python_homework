import string
user_string = input('Please enter some text :')
arr = []
for i in user_string.title():
    if i not in string.punctuation and i != ' ':
        arr.append(i)
if len(arr) > 139:
    arr = arr[:139]
new_str = ''.join(arr)
hashtag = '#' + new_str
print(hashtag)
