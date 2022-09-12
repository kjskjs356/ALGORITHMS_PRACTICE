# 2573 빙산

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, v):
    stack = []
    stack.append((x, y))
    while stack:
        x2, y2 = stack.pop(0)
        for i in range(4):
            if 0 <= x2 + dx[i] <= N - 1 and 0 <= y2 + dy[i] <= M - 1:
                if v[x2 + dx[i]][y2 + dy[i]]:
                    continue
                else:
                    stack.append((x2 + dx[i], y2 + dy[i]))
                    v[x2 + dx[i]][y2 + dy[i]] = True
    return v

# 빙산 체크 함수
def check_field(field):
    cnt = 0
    visited = [[True] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if field[i][j] != 0:
                visited[i][j] = False
    # 덩어리 체크
    for x in range(N):
        for y in range(M):
            if field[x][y] == 0 or visited[x][y]:
                continue
            else:
                visited = bfs(x, y, visited)
                cnt += 1
    return cnt


# 빙산 녹는 함수
def melt_field(field):
    check = [[False] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if field[x][y] != 0:
                check[x][y] = True
    for x in range(N):
        for y in range(M):
            if field[x][y] != 0:
                # 4 방향 체크하면서 물이 있으면 빙산 1씩 감소
                for i in range(4):
                    if field[x][y] == 0:
                        break
                    if not(0 <= x + dx[i] <= N - 1 and 0 <= y + dy[i] <= M - 1):
                        continue
                    if field[x + dx[i]][y + dy[i]] == 0 and not check[x + dx[i]][y + dy[i]]:
                        field[x][y] -= 1
    return field

result = 0
while True:
    sum_field = 0
    cnt = check_field(field)
    if cnt >= 2:
        break
    field = melt_field(field)
    for i in range(N):
        sum_field += sum(field[i])
    if sum_field == 0:
        result = 0
        break
    result += 1
print(result)