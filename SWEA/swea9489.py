# 9489_고대 유적 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map_arr = []
    result = 0
    for _ in range(N):
        map_arr.append(list(map(int, input().split())))
    # 가로방향 체크
    for i in range(N):
        cnt = 0
        for j in range(M):
            if map_arr[i][j] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0
    # 세로방향 체크
    for i in range(M):
        cnt = 0
        for j in range(N):
            if map_arr[j][i] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0
    print('#{} {}' .format(tc, result))