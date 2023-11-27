import string


def is_palindrome(text):
    result = False
    arr = []
    for i in text:
        if i.isupper():
            arr.append(i.lower())
        elif i not in string.punctuation and i != ' ':
            arr.append(i)
    str = ''.join(arr)
    revers_str = str[::-1]
    if str == revers_str:
        result = True
    return result


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print('OK')
