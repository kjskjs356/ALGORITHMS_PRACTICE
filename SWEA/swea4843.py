# 4843 특별한 정렬 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    #버블 정렬 우선 시행
    for i in range(N - 1):
        for j in range(N - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result_arr = [0] * N
    n, m, l = 0, -1, 0
    is_odd = False
    is_even = True
    #리스트 길이만큼 반복 작업
    while n < N:
        if is_even:
            result_arr[n] = arr[m]
            is_even = False
            is_odd = True
            n += 1
            m -= 1
        elif is_odd:
            result_arr[n] = arr[l]
            is_odd = False
            is_even = True
            n += 1
            l += 1
    print('#{}' .format(tc), end=' ')
    for i in range(10):
        print(result_arr[i], end=' ')
    print()