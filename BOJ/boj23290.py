# 마법사 상어와 복제


def shark_move(x, y, arr):
    visited = [[False] * 4 for _ in range(4)]
    cnt = 0
    flag = True
    for d in arr:
        x += dx2[d]
        y += dy2[d]
        if 0 <= x < 4 and 0 <= y < 4:
            if not visited[x][y]:
                cnt += sum(area[x][y])
                visited[x][y] = True
        else:
            flag = False
            break
    return cnt, flag


def shark_best_move(x, y, arr):
    visited = [[False] * 4 for _ in range(4)]
    for d in arr:
        x += dx2[d]
        y += dy2[d]
        if sum(area[x][y]) > 0 and not visited[x][y]:
            visited[x][y] = True
            for i in range(len(area[x][y])):
                area[x][y][i] = 0
            smell[x][y] = 3
    return x, y


def fish_move():
    result = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            # 물고기 있으면 이동
            if sum(area[x][y]) > 0:
                # 각 물고기 방향 체크
                for d in range(len(area[x][y])):
                    if area[x][y][d] > 0:
                        is_move = True
                        origin_d = d
                        num = area[x][y][d]
                        for _ in range(8):
                            nx = x + dx1[d]
                            ny = y + dy1[d]
                            # 이동 가능
                            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y) and smell[nx][ny] == 0:
                                result[nx][ny][d] += num
                                is_move = False
                                break
                            else:
                                d = (d - 1) % 8
                        # 이동 못하면 제자리
                        if is_move:
                            result[x][y][origin_d] += num
    return result


def comb_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in comb_with_replacement(arr, r - 1):
                yield [arr[i]] + j


# 9시 부터 시계방향(인덱스 0: 9시)
dx1 = [0, -1, -1, -1, 0, 1, 1, 1]
dy1 = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 이동
dx2 = [-1, 0, 1, 0]
dy2 = [0, -1, 0, 1]

# 상: 0, 좌: 1, 하: 2, 우: 3
move = comb_with_replacement([0, 1, 2, 3], 3)
move_arr = []
for arr in move:
    move_arr.append(arr)
M, S = map(int, input().split())
area = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

for _ in range(M):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    area[x][y][d] += 1
shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1
smell = [[0 for _ in range(4)] for _ in range(4)]

for num in range(S):
    # 복제를 위한 클론 배열 생성
    clone = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(8):
                clone[i][j][k] += area[i][j][k]

    # 물고기 방향대로 이동
    area = fish_move()

    # 상어의 이동 루트 중 최적의 값 탐색
    max_cnt = -1
    for arr in move_arr:
        cnt, flag = shark_move(shark_x, shark_y, arr)
        if flag:
            if max_cnt < cnt:
                max_cnt = cnt
                best_arr = arr
    # 최적 방향으로 상어 이동
    shark_x, shark_y = shark_best_move(shark_x, shark_y, best_arr)

    # 냄새 갱신
    for x in range(4):
        for y in range(4):
            if smell[x][y] > 0:
                smell[x][y] -= 1

    # 복제 마법 시전
    for i in range(4):
        for j in range(4):
            for k in range(len(clone[i][j])):
                area[i][j][k] += clone[i][j][k]

# 격자에 있는 물고기수 체크
ans = 0
for i in range(4):
    for j in range(4):
        if area[i][j]:
            ans += sum(area[i][j])
print(ans)