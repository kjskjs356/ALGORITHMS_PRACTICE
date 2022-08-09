# 4835 sumofintervals 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_result = 0
    min_result = 0
    # 합 최솟값 우선 설정
    for j in range(0, M):
        min_result += arr[j]
    for i in range(0, N - M + 1):
        Sum = 0
        # 연속 M개 숫자합 체크하여 최대값, 최솟값 갱신
        for j in range(i, M + i):
            Sum += arr[j]
        if max_result < Sum:
            max_result = Sum
        if min_result > Sum:
            min_result = Sum
    print('#{} {}' .format(tc, (max_result - min_result)))