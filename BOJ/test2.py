arr = [[1,2],[4,5,6]]
for i in range(len(arr)):
    print(arr[i])
arr = list(map(list, zip(*arr[::-1])))
print(arr)