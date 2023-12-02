def popular_words(text, words):
    quantity = []
    result = {}
    separated_words = text.lower().split()
    for i in words:
        quantity.append(separated_words.count(i))
    for i in range(len(words)):
        result[words[i]] = quantity[i]
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

