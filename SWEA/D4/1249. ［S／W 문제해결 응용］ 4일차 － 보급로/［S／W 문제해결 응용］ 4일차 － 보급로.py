# 1249_보급로 풀이
# 2022-09-27

from collections import deque

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                tmp = dp[x][y] + area[nx][ny]
                if tmp < dp[nx][ny]:
                    dp[nx][ny] = tmp
                    q.append((nx, ny))
                else:
                    continue


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, list(input()))) for _ in range(N)]
    dp = [[float('inf')] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dp[0][0] = 0
    bfs()
    print('#{} {}' .format(tc, dp[N - 1][N - 1]))
