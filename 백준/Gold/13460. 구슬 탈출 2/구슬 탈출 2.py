# 13460 구슬 탈출2


def target_move(arr, x, y, n):
    if arr[x][y] == '.':
        return x, y
    s_x, s_y = x, y
    while True:
        nx = x + dx[n]
        ny = y + dy[n]
        if arr[nx][ny] == '.':
            x, y = nx, ny
        elif arr[nx][ny] == 'O':
            arr[s_x][s_y] = '.'
            x, y = nx, ny
            break
        else:
            arr[x][y], arr[s_x][s_y] = arr[s_x][s_y], arr[x][y]
            break
    return x, y


def move(arr, rx, ry, bx, by, n):
    # 남쪽
    if n == 0:
        if rx > bx:
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
        else:
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)

    # 북쪽
    elif n == 1:
        if rx < bx:
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
        else:
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
    # 동쪽
    elif n == 2:
        if ry > by:
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
        else:
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
    # 서쪽
    elif n == 3:
        if ry < by:
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
        else:
            # 파란공 이동
            bx, by = target_move(arr, bx, by, n)
            # 빨간공 이동
            rx, ry = target_move(arr, rx, ry, n)
    return rx, ry, bx, by


def back(arr, rx, ry, bx, by, gx, gy, cnt, direct):
    global ans
    if cnt >= ans or (bx == gx and by == gy) or cnt > 10:
        return
    if rx == gx and ry == gy:
        ans = min(ans, cnt)
        return
    for i in range(4):
        # 이동했던 방향으로 다시 돌아가는건 X
        if direct % 2 == 1:
            if direct - 1 == i: continue
        elif direct % 2 == 0:
            if direct + 1 == i: continue
        if rx + dx[i] == '#' and bx + dx[i] == '#' or ry + dy[i] == '#' and by + dy[i] == '#': continue
        area2 = [clone_arr[:] for clone_arr in arr]
        nrx, nry, nbx, nby = move(area2, rx, ry, bx, by, i)
        # for j in range(N):
        #     print(area2[j])
        # print()
        back(area2, nrx, nry, nbx, nby, gx, gy, cnt + 1, i)

N, M = map(int, input().split())
area = []
r_x, r_y = 0, 0
b_x, b_y = 0, 0
for i in range(N):
    arr = list(map(str, input()))
    for j in range(M):
        if arr[j] == 'R':
            r_x, r_y = i, j
        elif arr[j] == 'B':
            b_x, b_y = i, j
        elif arr[j] == 'O':
            g_x, g_y = i, j
    area.append(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = float('inf')
r_goal, b_goal = False, False
back(area, r_x, r_y, b_x, b_y, g_x, g_y, 0, 5)
if ans == float('inf'):
    print(-1)
else:
    print(ans)