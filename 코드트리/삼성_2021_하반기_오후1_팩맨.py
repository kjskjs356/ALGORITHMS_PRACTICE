import sys
sys.stdin = open('input.txt', 'r')

# 2021 삼성 하반기 오후 1번 팩맨

from collections import deque

m, t = map(int, input().split())
area = [[[] for _ in range(4)] for _ in range(4)]
death = [[0] * 4 for _ in range(4)]
ans = 0

#  몬스터 방향 델타 (12시부터 반시계방향)
dxm = [-1, -1, 0, 1, 1, 1, 0, -1]
dym = [0, -1, -1, -1, 0, 1, 1, 1]

# 팩맨 방향 델타 (상-좌-하-우 우선순위)
dxp = [-1, 0, 1, 0]
dyp = [0, -1, 0, 1]

r, c = map(int, input().split())
packman = [r -1, c - 1]

for _ in range(m):
    r, c, d = map(int, input().split())
    area[r - 1][c - 1].append(d - 1)


def CopyMonster():
    for i in range(4):
        for j in range(4):
            # 몬스터 존재여부 체크
            if area[i][j]:
                for mst in area[i][j]:
                    areaCopy[i][j].append(mst)

def MoveMonster():
    # 각 몬스터 자신의 방향으로 이동. 단, 이동할수없을 시 반시계방향으로 45도 회전
    area2 = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if area[x][y]:
                for d in area[x][y]:
                    flag = False
                    # 8방향 탐색(자신의 방향 우선)
                    for i in range(8):
                        nx = x + dxm[(d + i) % 8]
                        ny = y + dym[(d + i) % 8]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            # 시체가 있거나 팩맨이 있는 경우 제외하고 이동
                            if death[nx][ny] > 0 or [nx, ny] == packman: continue
                            area2[nx][ny].append((d + i) % 8)
                            flag = True
                            break
                    # 몬스터가 이동할 수 있는 경로가 없는 경우 현 위치 유지
                    if not flag:
                        area2[x][y].append(d)
    # 이동 마친 후 area2 -> area로 덮어쓰기
    for i in range(4):
        for j in range(4):
            area[i][j] = area2[i][j]

def back(x, y, cnt, eat):
    global bestMove, maxEat, none
    if cnt == 3:
        if eat > maxEat:
            bestMove = move[:]
            maxEat = eat
        elif eat == 0 and maxEat == 0 and not none:
            bestMove = move[:]
            none = True
        return
    for i in range(4):
        nx = x + dxp[i]
        ny = y + dyp[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny] == 0: eat += len(area[nx][ny])
            visited[nx][ny] += 1
            move.append([nx, ny])
            back(nx, ny, cnt + 1, eat)
            visited[nx][ny] -= 1
            if visited[nx][ny] == 0: eat -= len(area[nx][ny])
            move.pop()


def PackMove():
    global bestMove
    [x, y] = packman
    # 백트래킹으로 팩맨 경로 탐색 후 최적 경로 계산
    back(x, y, 0, 0)
    packman[0], packman[1] = bestMove[2]
    # 경로마다 몬스터 존재 시 먹기
    for route in bestMove:
        [i, j] = route
        if area[i][j]:
            death[i][j] = 3
            area[i][j] = []


def CheckDeath():
    for i in range(4):
        for j in range(4):
            if death[i][j] > 0: death[i][j] -= 1

for _ in range(t):
    # 몬스터 복제 시도
    areaCopy = [[[] for _ in range(4)] for _ in range(4)]
    CopyMonster()
    # 몬스터 이동
    MoveMonster()
    # 팩맨이동
    move = []
    bestMove = []
    maxEat = 0
    visited = [[0] * 4 for _ in range(4)]
    [x, y] = packman
    none = False
    PackMove()
    # 시체 체크
    CheckDeath()
    # 복제 완성
    for i in range(4):
        for j in range(4):
            if areaCopy[i][j]:
                for mst in areaCopy[i][j]:
                    area[i][j].append(mst)

# 살아남은 몬스터 출력
for i in range(4):
    for j in range(4):
        if area[i][j]:
            ans += len(area[i][j])
print(ans)