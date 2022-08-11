# 1966 숫자를 정렬하자 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr) - 1):
        for j in range(len(arr)- 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print('#{}' .format(tc), end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()