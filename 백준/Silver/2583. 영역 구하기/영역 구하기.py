# 2583 영역 구하기

from collections import  deque


def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= M - 1 and 0 <= ny <= N - 1 and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt


M, N, K = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(M)]
arr = []
ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            ans += 1
            board[i][j] = 1
            arr.append(bfs(i, j))
arr.sort()
print(ans)
print(' '.join(map(str, arr)))