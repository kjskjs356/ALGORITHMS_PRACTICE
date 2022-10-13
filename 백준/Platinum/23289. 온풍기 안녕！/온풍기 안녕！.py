# 온풍기 안녕! 풀이

from collections import deque


def control(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 벗어나지 않은 경우 체크
        if 0 <= nx < R and 0 <= ny < C:
            # 벽에 막혀있으면 패스
            if i in wall[x][y]:
                continue
            # 인접 칸이 큰 쪽에서 짝은 쪽으로 조절
            else:
                if new_area2[x][y] > new_area2[nx][ny]:
                    tmp = (new_area2[x][y] - new_area2[nx][ny]) // 4
                    new_area[x][y] -= tmp
                    new_area[nx][ny] += tmp


def bfs(a, b, d, cnt):
    q = deque()
    q.append((a, b, cnt))
    while q:
        # 온풍기 바람세기 0되면 중지
        x, y, cnt = q.popleft()
        if cnt == 0:
            break
        for i in range(3):
            # 벽 체크를 위한 좌표
            nx1 = x + dx1[d][i]
            ny1 = y + dy1[d][i]
            #도착 좌표
            nx2 = x + dx2[d][i]
            ny2 = y + dy2[d][i]
            if 0 <= nx2 < R and 0 <= ny2 < C:
                # 벽 막힘 여부 확인
                if i == 0:
                    if (d + 1) % 4 in wall[x][y] or d in wall[nx1][ny1]:
                        continue
                    else:
                        if not visited[nx2][ny2]:
                            visited[nx2][ny2] = True
                            new_area[nx2][ny2] += cnt
                            q.append((nx2, ny2, cnt - 1))
                elif i == 1:
                    if d in wall[x][y]:
                        continue
                    else:
                        if not visited[nx2][ny2]:
                            visited[nx2][ny2] = True
                            new_area[nx2][ny2] += cnt
                            q.append((nx2, ny2, cnt - 1))
                elif i == 2:
                    if (d - 1) % 4 in wall[x][y] or d in wall[nx1][ny1]:
                        continue
                    else:
                        if not visited[nx2][ny2]:
                            visited[nx2][ny2] = True
                            new_area[nx2][ny2] += cnt
                            q.append((nx2, ny2, cnt - 1))
        cnt -= 1

# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 오른쪽, 위쪽, 왼쪽, 아래쪽
dx1 = [[-1, 0, 1], [0, -1, 0], [1, 0, -1], [0, 1, 0]]
dy1 = [[0, 1, 0], [-1, 0, 1], [0, -1, 0], [1, 0, -1]]

dx2 = [[-1, 0, 1], [-1, -1, -1], [1, 0, -1], [1, 1, 1]]
dy2 = [[1, 1, 1], [-1, 0, 1], [-1, -1, -1], [1, 0, -1]]

R, C, K = map(int, input().split())
check = []
heater = []
# 1 ~ 4는 온풍기가 향하는 방향을 숫자로 표시
# 0: 빈칸, 1: 오른쪽, 2: 왼쪽, 3: 위쪽, 4: 아래쪽, 5: 온도 조사 칸
area = []
ans = 0

for i in range(R):
    area.append(list(map(int, input().split())))
    for j in range(C):
        if area[i][j] == 5:
            check.append((i, j))
        elif area[i][j] > 0:
            heater.append((i, j, area[i][j]))
W = int(input())
# wall = dict()
wall = [[[] for _ in range(C)] for _ in range(R)]
# 벽 데이터 생성
for _ in range(W):
    # t = 0 : x, y 좌표 기준 위쪽과 벽 존재
    # t = 1 : x, y 좌표 기준 오른쪽과 벽 존재
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall[x][y].append(1)
        wall[x - 1][y].append(3)
    else:
        wall[x][y].append(0)
        wall[x][y + 1].append(2)
# 히터 순서대로 작동
new_area = [[0] * C for _ in range(R)]
flag = True
while flag:
    # 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽
    for x, y, d in heater:
        visited = [[False] * C for _ in range(R)]
        if d == 2:
            d = 3
        elif d == 3:
            d = 2
        d -= 1
        nx = x + dx1[d][1]
        ny = y + dy1[d][1]
        new_area[nx][ny] += 5
        bfs(nx, ny, d, 4)
    # 온도 조절
    new_area2 = [arr[:] for arr in new_area]
    for i in range(R):
        for j in range(C):
            if new_area2[i][j] > 0:
                control(i, j)
    # 가장바깥쪽 칸 1씩 제거
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                if new_area[i][j] > 0:
                    new_area[i][j] -= 1

    # 초콜렛 섭취
    ans += 1
    # 초콜렛 먹은 수 100 넘어가면 중단
    if ans > 100:
        ans = 101
        break

    # 조사칸 확인 후 초콜렛 섭취
    flag = False
    for x, y in check:
        if new_area[x][y] < K:
            flag = True
print(ans)