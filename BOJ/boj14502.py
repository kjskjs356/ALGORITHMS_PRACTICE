# 14502 연구소 풀이

from collections import deque


def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if field[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    field[nx][ny] = 2
                    q.append((nx, ny))


# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
# 바이러스 위치 저장
virus = []
# 벽을 세울 수 있는 위치 저장
walls = []
field = []
max_safe = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    field.append(tmp)
    for j in range(M):
        if field[i][j] == 2:
            virus.append((i, j))
        elif field[i][j] == 0:
            walls.append((i, j))

# 조합을 활용하여 벽생성
for wall in comb(walls, 3):
    safe = 0
    visited = [[False] * M for _ in range(N)]
    for x, y in wall:
        field[x][y] = 1

    # 바이러스 심기
    for x, y in virus:
        field[x][y] = 2

    # bfs 탐색 후 안전영역 최대 크기 비교
    for x, y in virus:
        bfs(x, y)
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                safe += 1
        if max_safe < safe:
            max_safe = safe

    # 세웠던 벽, 바이러스 초기화
    for x, y in wall:
        field[x][y] = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 2:
                field[i][j] = 0
print(max_safe)
