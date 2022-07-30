# 9367_점점 커지는 당근의 수 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    max_cnt = 1
    result = 1
    #순회하여 연속 기록 갱신
    for i in range(0, len(C) - 1):
        if C[i] < C[i + 1]:
            max_cnt += 1
        else:
            max_cnt = 1
        if result < max_cnt:
            result = max_cnt
    print('#{} {}' .format(tc, result))