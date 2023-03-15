# 15685 드래곤 커브
from collections import deque

# 커브의 개수
N = int(input())
board = [[0] * 101 for _ in range(101)]

# 문제에서의 x, y와 코드에서의 x, y 서로반대
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ans = 0

for _ in range(N):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    q = deque()
    q.append(d)
    cnt = 0
    while cnt < g:
        length = len(q)
        for i in range(length - 1, -1, -1):
            q.append(q[i] + 1)
        cnt += 1
    # q에 들어있는 정보대로 드래곤 커브 시행
    while q:
        d = q.popleft()
        x += dx[d % 4]
        y += dy[d % 4]
        board[x][y] = 1

# 격자 검사
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
            ans += 1
print(ans)