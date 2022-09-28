# 미세먼지 안녕! 풀이


def diffusion(micro):
    for arr in micro:
        x, y = arr
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= R - 1 and 0 <= ny <= C - 1:
                if area[nx][ny] == -1:
                    continue
                area[nx][ny] += micro.get(arr) // 5
                area[x][y] -= micro.get(arr) // 5
            if area[x][y] < 0:
                area[x][y] = 0


def clear():
    first, second = micro_filter[0], micro_filter[1]

    #첫번 쨰 위치
    for i in range(first - 1, -1, -1):
        if i == 0:
            area[i][0] = 0
        else:
            area[i][0] = area[i - 1][0]

    for i in range(C):
        if i == C - 1:
            area[0][i] = 0
        else:
            area[0][i] = area[0][i + 1]

    for i in range(first + 1):
        if i == first:
            area[i][C - 1] = 0
        else:
            area[i][C - 1] = area[i + 1][C - 1]

    for i in range(C - 1, 0, -1):
        if i == 1:
            area[first][i] = 0
        else:
            area[first][i] = area[first][i - 1]

    #두번 째 위치
    for i in range(second + 1, R):
        if i == R - 1:
            area[i][0] = 0
        else:
            area[i][0] = area[i+ 1][0]

    for i in range(C):
        if i == C - 1:
            area[R - 1][i] = 0
        else:
            area[R - 1][i] = area[R - 1][i + 1]

    for i in range(R - 1, second, -1):
        if i == second:
            area[i][C - 1] = 0
        else:
            area[i][C - 1] = area[i - 1][C - 1]

    for i in range(C - 1, 0, -1):
        if i == 1:
            area[second][i] = 0
        else:
            area[second][i] = area[second][i - 1]


# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# R, C : R x C 면적, T: 시간
R, C, T = map(int, input().split())
area = []
micro_filter = []
for i in range(R):
    area.append(list(map(int, input().split())))
    for j in range(len(area[i])):
        if area[i][j] == -1:
            micro_filter.append(i)
# T 초간 반복
for _ in range(T):
    # 현재 미세먼지 존재하는 곳 체크
    micro = dict()
    for i in range(R):
        for j in range(C):
            if area[i][j] > 0:
                micro[(i, j)] = area[i][j]
    # 먼지 확산
    diffusion(micro)
    # 확산 끝난 후 공기청정
    clear()

result = 0
for i in range(R):
    result += sum(area[i])
if result < 0:
    result = 0
else:
    result += 2
print(result)
