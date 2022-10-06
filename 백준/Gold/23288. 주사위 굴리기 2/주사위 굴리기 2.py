# 주사위 굴리기2 풀이

from collections import deque


def bfs(a, b):
    cnt = 1
    num = area[a][b]
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and area[nx][ny] == num:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    return cnt


def move(d):
    if d == 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = \
        dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = \
        dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = \
        dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = \
        dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]


# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 인덱스 - 0: 주사위 윗면, 5: 주사위 아랫면
dice = [1, 2, 3, 4, 5, 6]
x, y = 0, 0
# 첫 방향은 동쪽
d = 0
for _ in range(K):
    visited = [[False] * M for _ in range(N)]
    nx = x + dx[d % 4]
    ny = y + dy[d % 4]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        d += 2
        x += dx[d % 4]
        y += dy[d % 4]
    # 이동한 방향으로 주사위 상태 변경
    move(d % 4)
    cnt = bfs(x, y)
    ans += cnt * area[x][y]
    # 지도 칸과 주사위 값 비교하여 다음 방향결정
    if dice[5] > area[x][y]:
        d += 1
    elif dice[5] < area[x][y]:
        d -= 1
print(ans)