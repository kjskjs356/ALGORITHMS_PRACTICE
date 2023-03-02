# 1926 그림

from collections import  deque


def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and board[nx][ny] == 1:
                board[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arr = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            arr.append(bfs(i, j))
if arr:
    print(len(arr))
    print(max(arr))
else:
    print(0)
    print(0)