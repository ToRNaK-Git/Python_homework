def correct_sentence(text):
    arr = []
    if text[0].islower():
        arr.append(text[0].upper())
    else:
        arr.append(text[0])
    arr.append(text[1:])
    if text[-1] != '.':
        arr.append('.')
    return ''.join(arr)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
