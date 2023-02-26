# 18870 좌표 압축

N = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(list(set(arr)))
zip_list = {arr_sort[i]: i for i in range(len(arr_sort))}
for x in arr:
    print(zip_list[x], end=' ')
