# 온풍기 안녕! 풀이

from collections import deque

def bfs(a, b, d, cnt):
    q = deque()
    q.append((a, b, cnt))
    while q:
        # 온풍기 바람세기 0되면 중지
        x, y, cnt = q.popleft()
        for i in range(3):
            nx = x + dx[d][i]
            nx2 = x + dx2[d][i]
            ny = y + dy[d][i]
            ny2 = y + dy2[d][i]
            if 0 <= nx < R and 0 <= ny < C:
                # 벽에 막혀 있는지 확인
                print(wall.get((x, y)) == (nx2, ny2), wall.get((nx2, ny2)) == (x, y))
                if wall.get((x, y)) == (nx2, ny2) or wall.get((nx2, ny2)) == (x, y):
                    continue
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        new_area[nx][ny] += cnt
                        q.append((nx, ny, cnt - 1))
        cnt -= 1

# 오른쪽, 왼쪽, 위쪽, 아래쪽
dx = [[-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
dy = [[1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]

dx2 = [[-1, 0, 1], [-1, 0, 1], [0, -1, 0], [0, 1, 0]]
dy2 = [[0, 1, 0], [0, -1, 0], [-1, 0, 1], [-1, 0, 1]]

R, C, K = map(int, input().split())
check = []
heater = []
# 1 ~ 4는 온풍기가 향하는 방향을 숫자로 표시
# 0: 빈칸, 1: 오른쪽, 2: 왼쪽, 3: 위쪽, 4: 아래쪽, 5: 온도 조사 칸
area = []
new_area = [[0] * C for _ in range(R)]
for i in range(R):
    area.append(list(map(int, input().split())))
    for j in range(C):
        if area[i][j] == 5:
            check.append((i, j))
        elif area[i][j] > 0:
            heater.append((i, j, area[i][j]))

W = int(input())
wall = dict()
# 벽 데이터 생성
for _ in range(W):
    # t = 0 : x, y 좌표 기준 위쪽과 벽 존재
    # t = 1 : x, y 좌표 기준 오른쪽과 벽 존재
    x, y, t = map(int, input().split())
    if t == 0:
        wall[(x, y)] = (x - 1, y)
    elif t == 1:
        wall[(x, y)] = (x, y + 1)
# 히터 순서대로 작동
print(wall)
print(heater)
print()
for x, y, d in heater:
    visited = [[False] * C for _ in range(R)]
    print(x, y)
    d -= 1
    nx = x + dx[d][1]
    ny = y + dy[d][1]
    print(nx, ny)
    new_area[nx][ny] += 5
    bfs(nx, ny, d, 4)
    for i in range(R):
        print(new_area[i])
    print()

# 온도 조절
new_area2 = [arr[:] for arr in new_area]
for i in range(R):
    for j in range(C):
        if new_area2[i][j] > 0:
            pass