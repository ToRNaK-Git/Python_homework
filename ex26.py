def is_even(number):
    string = str(number)
    even_nums = [0, 2, 4, 6, 8]
    result = False
    for i in even_nums:
        if str(i) == string[-1]:
            result = True
    return result


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
