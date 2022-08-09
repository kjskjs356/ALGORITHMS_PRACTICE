# 4828 min_max 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

def func_max(arr):
    result = arr[0]
    for num in arr:
        if result < num:
            result = num
    return result

def func_min(arr):
    result = arr[0]
    for num in arr:
        if result > num:
            result = num
    return result

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    num = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    result = func_max(arr) - func_min(arr)
    print(f'#{tc} {result}')