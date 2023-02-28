# 1012 유기농 배추
from collections import deque

def bfs(a, b, v):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1 and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    ans = 0
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    # 배추밭 탐색
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] == 1:
                visited[i][j] = True
                ans += 1
                bfs(i, j, visited)
    print(ans)
