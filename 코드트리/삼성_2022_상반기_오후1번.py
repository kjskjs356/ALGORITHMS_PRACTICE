import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 상반기 오후 1번 꼬리잡기 놀이

from collections import deque

n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
ans = 0
lineNum = 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs2(a, b):
    q = deque()
    q.append((a, b))
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    hx, hy, tx, ty = -1, -1, -1, -1
    isHead, isTale = False, False
    while q:
        x, y = q.popleft()
        # 머리 좌표 저장
        if area[x][y] == 1:
            hx, hy = x, y
            isHead = True
        elif area[x][y] == 3:
            tx, ty = x, y
            isTale = True
        # 머리, 꼬리 둘다 찾았으면 자리 바꾼 후 종료
        if isHead and isTale:
            area[hx][hy], area[tx][ty] = area[tx][ty], area[hx][hy]
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if 1 <= area[nx][ny] <= 3 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def bfs(a, b):
    q = deque()
    q.append((a, b, 1))
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    while q:
        x, y, cnt = q.popleft()
        if area[x][y] == 1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] == 1 and not visited[nx][ny]:
                    if area[x][y] == 3: continue
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny, cnt + 1))
                elif area[nx][ny] == 2 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
                elif area[nx][ny] == 3 and not visited[nx][ny]:
                    visited[nx][ny] = True

def ThrowBall(x, y, d):
    # d 방향으로 진행하면서 사람 맞추기
    while True:
        if 0 <= x < n and 0 <= y < n:
            if 1 <= area[x][y] <= 3:
                num = bfs(x, y)
                return x, y, num
            else:
                x += dx[d]
                y += dy[d]
        else: return -1, -1, 0


# 총 k라운드 진행
for rnd in range(1, k + 1):
    visited = [[False] * n for _ in range(n)]
    # 팀마다 한칸씩 이동
    for a in range(n):
        for b in range(n):
            # 꼬리사람 찾기
            if area[a][b] == 3 and not visited[a][b]:
                num = 3
                visited[a][b] = True
                x, y = a, b
                # 몸통방향 찾아 이동하기
                breaker = False
                while True:
                    if breaker: break
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            # 꼬리에서 몸통으로 진행
                            if num == 3 and area[nx][ny] == 2:
                                visited[nx][ny] = True
                                area[x][y] = 4
                                area[nx][ny] = 3
                                num = 2
                                x, y = nx, ny
                                break
                            # 몸통이 계속되는 경우 좌표만 갱신
                            elif num == 2 and area[nx][ny] == 2:
                                visited[nx][ny] = True
                                x, y = nx, ny
                                break
                            # 머리에 도달한 경우 루프 탈출
                            elif num == 2 and area[nx][ny] == 1:
                                visited[nx][ny] = True
                                area[nx][ny] = 2
                                num = 1
                                x, y = nx, ny
                                breaker = True
                                break
                # 머리 이동
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == 4:
                        visited[nx][ny] = True
                        area[nx][ny] = 1
                        break

    # 라운드에 따른 공 던지기(4n 주기로 원점)
    if lineNum == 4 * n + 1: lineNum = 1
    d = 0
    # 왼쪽 시작
    if 0 < lineNum <= n:
        d = 0
        x, y = lineNum - 1, 0
    # 아래쪽 시작
    elif n < lineNum <= 2 * n:
        d = 1
        x, y = n - 1, lineNum - n - 1
    # 오른쪽 시작
    elif 2 * n < lineNum <= 3 * n:
        d = 2
        x, y = 3 * n - lineNum, n - 1
    # 위쪽 시작
    elif 3 * n < lineNum <= 4 * n:
        d = 3
        x, y = 0, 4 * n - lineNum
    tx, ty, cnt = ThrowBall(x, y, d)
    # 점수를 못받았을 경우 다음 라운드 진행
    lineNum += 1
    if tx == -1 and ty == -1: continue
    ans += cnt**2
    # 점수 받은 팀의 머리-꼬리 위치 바꾸기
    bfs2(tx, ty)

print(ans)