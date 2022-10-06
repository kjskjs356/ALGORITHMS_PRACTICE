# 마법사 상어와 블리자드
"""
상어 = 0
구슬 폭발 후 앞 번호로 당기기

연속 구슬의 그룹이란?
11 111
22 222
이런식으로 동일한 숫자가 연속되는 그룹
ex) 111 의 경우
구슬의 개수 3, 구슬의 번호 1
A, B = 3, 1
"""

from collections import deque


def move(x, y, d):
    if x > (N - 1) // 2:
        if x == y or x == (N - 1 - y):
            d += 1
            x += dxx[d % 4]
            y += dyy[d % 4]
        else:
            x += dxx[d % 4]
            y += dyy[d % 4]
    else:
        if (x - 1) == y or x == (N - 1 - y):
            d += 1
            x += dxx[d % 4]
            y += dyy[d % 4]
        else:
            x += dxx[d % 4]
            y += dyy[d % 4]
    return x, y, d % 4


def sort_arr():
    x, y, d = N // 2, (N - 2) // 2, 0
    # 바꿀 좌표의 값
    x2, y2, d2 = x + 1, y, 1
    while 0 <= x2 < N and 0 <= y2 < N:
        if area[x][y] == 0:
            while area[x2][y2] == 0:
                x2, y2, d2 = move(x2, y2, d2)
                if not(0 <= x2 < N and 0 <= y2 < N):
                    break
            if not (0 <= x2 < N and 0 <= y2 < N):
                break
            area[x][y], area[x2][y2] = area[x2][y2], area[x][y]
        x, y, d = move(x, y, d)
        x2, y2, d2 = move(x2, y2, d2)
    return


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정렬용 델타방향
dxx = [0, 1, 0, -1]
dyy = [-1, 0, 1, 0]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for _ in range(M):
    x, y = N // 2, N // 2
    if area[x][y - 1] == 0:
        break
    stack = []
    d, s = map(int, input().split())
    d -= 1
    # 블리자드 마법 시전
    for num in range(1, s + 1):
        nx = x + dx[d] * num
        ny = y + dy[d] * num
        area[nx][ny] = 0
    # 구슬 파괴 후 정렬
    sort_arr()
    # 4개 이상 연속인 구슬이 존재하지 않을때까지 폭발 & 정렬 반복
    is_bomb = True
    while is_bomb:
        is_bomb = False
        x, y, d = N // 2, (N - 2) // 2, 0
        if area[x][y] == 0:
            break
        stack.append((x, y))
        x, y, d = move(x, y, d)
        while 0 <= x < N and 0 <= y < N:
            if area[x][y] == 0:
                break
            if area[x][y] == area[stack[0][0]][stack[0][1]]:
                stack.append((x, y))
                x, y, d = move(x, y, d)
            else:
                # 4개 이상이면 폭발
                if len(stack) >= 4:
                    ans += len(stack) * area[stack[0][0]][stack[0][1]]
                    is_bomb = True
                    for a, b in stack:
                        area[a][b] = 0
                    stack = []
                    stack.append((x, y))
                    x, y, d = move(x, y, d)
                else:
                    stack = []
                    stack.append((x, y))
                    x, y, d = move(x, y, d)
        # 끝에 도달한 경우(혹은 0에 도착한 경우) 스택에 4개이상 있으면 폭발
        if len(stack) >= 4:
            ans += len(stack) * area[stack[0][0]][stack[0][1]]
            is_bomb = True
            for a, b in stack:
                area[a][b] = 0
        stack = []
        sort_arr()

    # 구슬을 그룹지어서 새롭게 배치
    new_area = [[0] * N for _ in range(N)]
    stack2 = deque()
    x, y, d = N // 2, (N - 2) // 2, 0
    if area[x][y] == 0:
        break
    stack.append((x, y))
    x, y, d = move(x, y, d)
    while 0 <= x < N and 0 <= y < N:
        if area[x][y] == 0:
            break
        if area[x][y] == area[stack[0][0]][stack[0][1]]:
            stack.append((x, y))
            x, y, d = move(x, y, d)
        else:
            stack2.append(len(stack))
            stack2.append(area[stack[0][0]][stack[0][1]])
            stack = []
            stack.append((x, y))
            x, y, d = move(x, y, d)
    if stack:
        stack2.append(len(stack))
        stack2.append(area[stack[0][0]][stack[0][1]])
    x, y, d = N // 2, (N - 2) // 2, 0
    while (0 <= x < N and 0 <= y < N) and stack2:
        new_area[x][y] = stack2.popleft()
        x, y, d = move(x, y, d)
    area = [arr[:] for arr in new_area]
print(ans)