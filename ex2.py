arr = [0, 1, 7, 2, 4, 8]
sumy = 0
if arr:
    for i in range(len(arr)):
        if i % 2 == 0:
            sumy = sumy + arr[i]
    sumy = sumy * arr[-1]
print(sumy)