# 2667 단지번호 붙이기

from collections import deque

N = int(input())
board = [list(map(int, str(input()))) for _ in range(N)]

# 총 단자 수
ans = 0
# 단자 별 건물 수
arr = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt


for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            ans += 1
            board[i][j] = 0
            cnt = bfs(i, j)
            arr.append(cnt)
arr.sort()
print(ans)
for cnt in arr:
    print(cnt)