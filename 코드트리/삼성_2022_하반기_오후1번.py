import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 하반기 오후 1번 코드트리 빵

from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
store = []
storeCheck = [0] * m
personCheck = [False] * m
location = []
for _ in range(m):
    x, y = map(int, input().split())
    store.append([x - 1, y - 1])

# 편의점에서 가까운 베이스캠프 찾는 델타탐색
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 1. 사람 순서대로 베이스캠프에서 store 배열에 저장되어있는 편의점 좌표로 1칸씩 최단거리로 이동
# 상, 우, 좌, 하 우선순위
# 아직 베이스캠프에 없는 사람은 패스
# t분마다 행동실행, 최초는 t = 0분부터 진행(인덱스 0번부터 시작)


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        # 가장 가까운 베이스캠프 좌표 발견 시
        if area[x][y] == 1:
            return x, y
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


def bfs2(rx, ry, a, b):
    q = deque()
    q.append((a, b, 0))
    visited = [[False] * n for _ in range(n)]
    areaDist = [[99] * n for _ in range(n)]
    visited[a][b] = True
    areaDist[a][b] = 0
    while q:
        # 좌표별 거리 탐색
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and area[nx][ny] != -1:
                    visited[nx][ny] = True
                    areaDist[nx][ny] = cnt + 1
                    q.append((nx, ny, cnt + 1))
    # 현재 위치 기준 가장 가까운 방향 설정
    minDist = 99
    direct = 0
    for i in range(4):
        nx = rx + dx[i]
        ny = ry + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if areaDist[nx][ny] < minDist:
                minDist = areaDist[nx][ny]
                direct = i
    return direct

def MoveAll():
    for i in range(m):
        # 아직 배치안된 사람 패스 & 편의점 도착한 사람 패스
        if not personCheck[i]: continue
        if storeCheck[i] == 1: continue
        # 1번(인덱스 0)사람부터 최단거리 탐색
        x1, y1, x2, y2 = location[i][0], location[i][1], store[i][0], store[i][1]
        d = bfs2(x1, y1, x2, y2)
        nx = x1 + dx[d]
        ny = y1 + dy[d]
        location[i] = [nx, ny]

def CantMove():
    for i in range(len(location)):
        if storeCheck[i] == 1: continue
        x, y = store[i][0], store[i][1]
        # 해당 사람의 위치가 편의점에 위치와 동일하면 방문처리
        if location[i] == [x, y]:
            area[x][y] = -1
            storeCheck[i] = 1


def SelectCamp(idx):
    a, b = store[idx][0], store[idx][1]
    # 해당 편의점에서 가까운 캠프 탐색
    x, y = bfs(a, b)
    # 사람 배치
    personCheck[idx] = True
    location.append([x, y])
    # 해당 베이스캠프 접근금지
    area[x][y] = -1



t = -1

while True:
    t += 1
    # 격자에 존재하는 모든 사람 이동
    MoveAll()

    # 이동을 마친 후 방문한 편의점 이동 못하게 설정
    CantMove()
    # 모든 사람이 편의점 도착 시 종료
    if sum(storeCheck) == m:
        break

    # t번째 해당하는 사람 베이스캠프 지정(마지막 사람까지 지정되면 종료)
    if t < m:  SelectCamp(t)
print(t + 1)