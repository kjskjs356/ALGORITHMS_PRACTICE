import sys
sys.stdin = open('input.txt', 'r')

# 2021 삼성 하반기 오전 2번 냉방시스템

from collections import deque

n, m, k = map(int, input().split())
wind = []
area = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] > 1:
            wind.append([i, j, temp[j]])
    area.append(temp)
t = 1
wall = [[[] for _ in range(n)] for _ in range(n)]
condition = [[0] * n for _ in range(n)]

# 시원함 전파 델타(서-북-동-남)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 에어컨 동서남북 딕셔너리(2: 왼쪽, 3: 위쪽, 4: 오른쪽, 5: 아래쪽 향함)
dxw = {
    2: [-1, 0, 1],
    3: [-1, -1, -1],
    4: [-1, 0, 1],
    5: [1, 1, 1],
}
dyw = {
    2: [-1, -1, -1],
    3: [-1, 0, 1],
    4: [1, 1, 1],
    5: [-1, 0, 1],
}

for _ in range(m):
    x, y, s = map(int, input().split())
    # wall값 - 1, 3: 벽이 왼쪽 or 오른쪽 / 0, 2: 벽이 위쪽 or 아래쪽
    if s == 1:
        wall[x - 1][y - 1].append(1)
        wall[x - 1][y - 2].append(3)
    elif s == 0:
        wall[x - 1][y - 1].append(0)
        wall[x - 2][y - 1].append(2)

def SubCool(a, b, d, cnt):
    q= deque()
    q.append((a, b, cnt))
    visited = [[False] * n for _ in range(n)]
    while q:
        x, y, cnt = q.popleft()
        for i in range(3):
            nx = x + dxw[d][i]
            ny = y + dyw[d][i]
            # 왼쪽 향함
            if 0 <= nx < n and 0 <= ny < n:
                if d == 2:
                    if i == 0:
                        if 0 not in wall[x][y] and 3 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 1:
                        if 1 not in wall[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 2:
                        if 2 not in wall[x][y] and 3 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                # 위쪽 향함
                if d == 3:
                    if i == 0:
                        if 1 not in wall[x][y] and 2 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 1:
                        if 0 not in wall[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 2:
                        if 3 not in wall[x][y] and 2 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                # 오른쪽 향함
                if d == 4:
                    if i == 0:
                        if 0 not in wall[x][y] and 1 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 1:
                        if 3 not in wall[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 2:
                        if 2 not in wall[x][y] and 1 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                # 아래쪽 향함
                if d == 5:
                    if i == 0:
                        if 1 not in wall[x][y] and 0 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 1:
                        if 2 not in wall[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))
                    elif i == 2:
                        if 3 not in wall[x][y] and 0 not in wall[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            condition[nx][ny] += cnt - 1
                            if cnt > 2: q.append((nx, ny, cnt - 1))

def Cooling(idx):
    x, y, direct = wind[idx]
    x += dx[direct - 2]
    y += dy[direct - 2]
    condition[x][y] += 5
    # 방향에 따라 벽 확인 후 확산
    SubCool(x, y, direct, 5)


def Diffuse():
    # 각 칸마다 체크
    for x in range(n):
        for y in range(n):
            # 서-북-동-남
            # wall값 - 1, 3: 벽이 왼쪽 or 오른쪽 / 0, 2: 벽이 위쪽 or 아래쪽
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    # 벽에 막혀있으면 불가
                    if i == 0 and 1 in wall[x][y]: continue
                    if i == 1 and 0 in wall[x][y]: continue
                    if i == 2 and 3 in wall[x][y]: continue
                    if i == 3 and 2 in wall[x][y]: continue
                    temp = condition[x][y] - condition[nx][ny]
                    if temp >= 4:
                        cnt = temp // 4
                        condition2[nx][ny] += cnt
                        condition2[x][y] -= cnt

    # condition2 -> conditon 동기화, 외벽의 경우 1씩 감소
    for x in range(n):
        for y in range(n):
            condition[x][y] = condition2[x][y]
            if x == 0 or x == n - 1 or y == 0 or y == n - 1:
                if condition[x][y] > 0: condition[x][y] -= 1

def Check():
    flag = True
    breaker = False
    for i in range(n):
        if breaker: break
        for j in range(n):
            if area[i][j] == 1:
                if condition[i][j] < k:
                    flag = False
                    breaker = True
                    break
    return flag

while True:
    if t > 100:
        t = -1
        break
    # 에어컨 순서대로 가동
    for i in range(len(wind)):
        Cooling(i)
    # 온도 확산
    condition2 = [arr[:] for arr in condition]
    Diffuse()
    # 사무실 온도 체크
    if Check():
        break
    t += 1
print(t)