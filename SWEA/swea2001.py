# 2001 파리 퇴치 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = []
    max_sum = 0
    kill_fly = 0
    for _ in range(N):
        fly_map.append(list(map(int, input().split())))
    #파리채 퇴치
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_fly = 0
            for k in range(i, M + i):
                for l in range(j, M + j):
                    kill_fly += fly_map[k][l]
            if max_sum < kill_fly:
                max_sum = kill_fly
    print('#{} {}' .format(tc, max_sum))
