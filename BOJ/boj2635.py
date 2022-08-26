# 2635 수 이어가기

def func_len(arr):
    cnt = 0
    for x in arr:
        cnt += 1
    return cnt

N = int(input())
result = 1

for i in range(N + 1):
    arr = [N, i]
    j = 0
    while True:
        tmp = arr[j] - arr[j + 1]
        if tmp >= 0:
            arr.append(tmp)
            j += 1
        else:
            break
    if result < func_len(arr):
        result = func_len(arr)
        result_arr = arr
print(result)
print(*result_arr)