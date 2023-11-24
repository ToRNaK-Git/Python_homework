import random


def common_elements():
    arr1 = []
    arr2 = []
    for i in range(random.randint(0, 200)):
        if i % 3 == 0:
            arr1.append(i)
    arr1 = set(arr1)
    for i in range(random.randint(0, 200)):
        if i % 5 == 0:
            arr2.append(i)
    arr2 = set(arr2)
    common = arr1.intersection(arr2)
    return common