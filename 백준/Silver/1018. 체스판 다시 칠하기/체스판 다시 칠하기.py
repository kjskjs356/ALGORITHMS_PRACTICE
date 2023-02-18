
# 1018 체스판 다시 칠하기
from collections import  deque

N, M = map(int, input().split())

board = [list(map(str, input()))for _ in range(N)]
ans = float('inf')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(a, b, arr):
    global visited, cnt
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if a <= nx <= a + 7 and b <= ny <= b + 7:
                if not visited[nx - a][ny - b]:
                    visited[nx - a][ny - b] = True
                    q.append((nx, ny))
                    if arr[nx][ny] != arr[x][y]:
                        continue
                    else:
                        if arr[x][y] == 'B':
                            arr[nx][ny] = 'W'
                        else:
                            arr[nx][ny] = 'B'
                        cnt += 1


# 각 칸을 기준으로 8x8 탐색
for i in range(N - 7):
    for j in range(M - 7):
        first_word = board[i][j]
        visited = [[False] * 8 for _ in range(8)]
        cnt = 0
        # bfs로 각 시작점에서 칠해야되는 부분 개수 구하기
        visited[0][0] = True
        board2 = [arr[:] for arr in board]
        bfs(i, j, board2)
        if ans > cnt:
            ans = cnt

        # 스타트 부분을 먼저 바꾸고 계산해보기
        visited = [[False] * 8 for _ in range(8)]
        cnt = 0
        visited[0][0] = True
        board3 = [arr[:] for arr in board]
        if first_word == 'W':
            board3[i][j] = 'B'
        else:
            board3[i][j] = 'W'
        cnt += 1
        bfs(i, j, board3)
        if ans > cnt:
            ans = cnt
print(ans)