# 1861_정사각형방 문제풀이
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(x, y, cnt):
    q.append((x, y))
    while q:
        # 4방향 탐색
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if field[nx][ny] - field[a][b] == 1:
                    cnt += 1
                    q.append((nx, ny))
                    break
    return cnt


# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    # tmp : 방 이동수 비교값, result : 방 이동수 최대값, num : 방 번호
    tmp, result, num = 0, 0, 9999999
    q = deque()
    for i in range(N):
        for j in range(N):
            tmp = bfs(i, j, 1)
            if result < tmp:
                result = tmp
                num = field[i][j]
            elif result == tmp:
                if num > field[i][j]:
                    num = field[i][j]
    print('#{} {} {}' .format(tc, num, result))
