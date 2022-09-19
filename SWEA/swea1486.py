# 1486_장훈이의 높은 선반 문제풀이
# 2022-09-16

import sys
sys.stdin = open('input.txt', 'r')


def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    result = 9999999
    for i in range(1, N + 1):
        arr = comb(H, i)
        for j in range(len(arr)):
            tmp = sum(arr[j])
            if tmp >= B:
                if result > tmp:
                    result = tmp
    print('#{} {}' .format(tc, result - B))
