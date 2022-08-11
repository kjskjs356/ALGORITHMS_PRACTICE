# 1979 어디에 단어가 들어있을까 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    result = 0
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    #가로 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
            if j == N - 1:
                if cnt == K:
                    result += 1
    # 세로 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
            if j == N - 1:
                if cnt == K:
                    result += 1
    print('#{} {}'.format(tc, result))