# 9386_연속한 1의 개수 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    result, cnt = 0, 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
            if result < cnt:
                result = cnt
        else:
            cnt = 0
    print('#{} {}' .format(tc, result))