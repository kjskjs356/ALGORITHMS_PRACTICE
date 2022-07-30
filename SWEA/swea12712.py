# 12712_파리퇴치3 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = []
    result = 0
    for _ in range(N):
        fly_map.append(list(map(int, input().split())))
    #파리 퇴치
    for i in range(N):
        for j in range(N):
            fly_sum = fly_map[i][j]
            for k in range(1, M):
                # 십자 합
                if 0 <= i + k <= N - 1: fly_sum += fly_map[i + k][j]
                if 0 <= i - k <= N - 1: fly_sum += fly_map[i - k][j]
                if 0 <= j + k <= N - 1: fly_sum += fly_map[i][j + k]
                if 0 <= j - k <= N - 1: fly_sum += fly_map[i][j - k]
            if result < fly_sum: result = fly_sum
            fly_sum = fly_map[i][j]
            for l in range(1, M):
                # X자 합
                if 0 <= i + l <= N - 1 and 0 <= j + l <= N - 1: fly_sum += fly_map[i + l][j + l]
                if 0 <= i + l <= N - 1 and 0 <= j - l <= N - 1: fly_sum += fly_map[i + l][j - l]
                if 0 <= i - l <= N - 1 and 0 <= j + l <= N - 1: fly_sum += fly_map[i - l][j + l]
                if 0 <= i - l <= N - 1 and 0 <= j - l <= N - 1: fly_sum += fly_map[i - l][j - l]
            if result < fly_sum: result = fly_sum
    print('#{} {}' .format(tc, result))