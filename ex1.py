arr = [0]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.remove(0)
        arr.append(0)
print(arr)
