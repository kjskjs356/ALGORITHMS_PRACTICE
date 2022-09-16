#20058 마법사 상어와 파이어스톰

from collections import deque

def bfs(a, b):
    n = 1
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= side - 1 and 0 <= ny <= side - 1:
                if ice[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    n += 1
    return n
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, Q = map(int, input().split())
# 한 변의 길이
side = 2**N
ice = [list(map(int, input().split())) for _ in range(side)]
L = list(map(int, input().split()))
result = 0
sum_ice = 0
visited = [[False] * side for _ in range(side)]
max_cnt = 0
for i in range(Q):
    ice_check = [[False] * side for _ in range(side)]
    # 격자당 길이
    length = 2**L[i]
    # 한 줄 당 격자 수
    num = side // length
    # 각 격자마다 체크
    for j in range(num):
        for k in range(num):
            # 각 격자마다의 넓이만큼 회전하기 위한 더미 복사
            tmp = [[0] * length for _ in range(length)]
            row, col = 0, 0
            for l in range(j * length, j * length + length):
                for m in range(k * length, k * length + length):
                    tmp[col][length - row - 1] = ice[l][m]
                    col += 1
                col = 0
                row += 1
            row, col = 0, 0
            # 회전 실행
            for l in range(j * length, j * length + length):
                for m in range(k * length, k * length + length):
                    ice[l][m] = tmp[row][col]
                    col += 1
                col = 0
                row += 1
            row, col = 0, 0

    # 회전 끝난 후 파이어스톰 시전
    for x in range(side):
        for y in range(side):
            if ice[x][y] != 0:
                ice_check[x][y] = True
    for x in range(side):
        for y in range(side):
            if ice[x][y] == 0:
                continue
            cnt = 0
            # 4 방향 탐색
            for direct in range(4):
                nx = x + dx[direct]
                ny = y + dy[direct]
                if 0 <= nx <= side - 1 and 0 <= ny <= side - 1:
                    if ice_check[nx][ny]:
                        cnt += 1
            if cnt < 3:
                if ice[x][y] > 0:
                    ice[x][y] -= 1

# 남아있는 얼음의 합
for j in range(side):
    sum_ice += sum(ice[j])

# 가장 큰 덩어리 칸의 개수 구하기 - bfs
for x in range(side):
    for y in range(side):
        if ice[x][y] != 0:
            val = bfs(x, y)
            if max_cnt < val:
                max_cnt = val
print(sum_ice)
print(max_cnt)