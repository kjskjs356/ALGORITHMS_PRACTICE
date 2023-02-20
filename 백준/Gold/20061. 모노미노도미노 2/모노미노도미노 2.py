
# 20061 모노미노도미노2

N = int(input())

# 보드 2개로 나누어 판단
board1 = [[0] * 4 for _ in range(10)]
board2 = [[0] * 4 for _ in range(10)]

ans = 0
block = 0


# 가로 줄 꽉 찬 경우 지우고 점수
def check_row(arr):
    global ans
    for i in range(9, -1, -1):
        if sum(arr[i]) == 4:
            ans += 1
            for j in range(4):
                arr[i][j] = 0
            # 나머지 한칸씩 내려오기
            for k in range(4):
                for l in range(i, 3, -1):
                    arr[l][k], arr[l - 1][k] = arr[l - 1][k], arr[l][k]
            return True
    return False


# 연한 칸에 블록있는 경우
def remove_block(arr):
    cnt = 0
    if sum(arr[4]) > 0:
        cnt += 1
    if sum(arr[5]) > 0:
        cnt += 1

    while cnt > 0:
        cnt -= 1
        # 맨 아래줄 우선 제거
        for i in range(4):
            arr[9][i] = 0
        # 나머지 한칸씩 내려오기
        for i in range(4):
            for j in range(8, 3, -1):
                arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

for _ in range(N):
    # t = 1: 1x1 블록 / t = 2: 1x2 블록 / t = 3: 2x1 블록
    # x, y = 좌표(x, y)
    t, x, y = map(int, input().split())

    # 블록의 종류(t)에 따라 배치 다르게
    if t == 1:
        board1[x][y] = 1
        board2[y][3 - x] = 1

        # 보드1 내리기
        idx = 6
        while board1[idx][y] == 0:
            idx += 1
            if idx == 10:
                break
        board1[x][y], board1[idx - 1][y] = board1[idx - 1][y], board1[x][y]

        # 보드2 내리기
        idx = 6
        while board2[idx][3 - x] == 0:
            idx += 1
            if idx == 10:
                break
        board2[y][3 - x], board2[idx - 1][3 - x] = board2[idx - 1][3 - x], board2[y][3 - x]

    elif t == 2:
        board1[x][y], board1[x][y + 1] = 1, 1
        board2[y][3 - x], board2[y + 1][3 - x] = 1, 1

        idx = 6
        while board1[idx][y] == 0 and board1[idx][y + 1] == 0:
            idx += 1
            if idx == 10:
                break
        board1[x][y], board1[idx - 1][y] = board1[idx - 1][y], board1[x][y]
        board1[x][y + 1], board1[idx - 1][y + 1] = board1[idx - 1][y + 1], board1[x][y + 1]

        idx = 6
        while board2[idx][3 - x] == 0:
            idx += 1
            if idx == 10:
                break
        board2[y][3 - x], board2[idx - 1][3 - x] = board2[idx - 1][3 - x], board2[y][3 - x]
        board2[y + 1][3 - x], board2[idx - 2][3 - x] = board2[idx - 2][3 - x], board2[y + 1][3 - x]

    elif t == 3:
        board1[x][y], board1[x + 1][y] = 1, 1
        board2[y][3 - x], board2[y][2 - x] = 1, 1

        idx = 6
        while board1[idx][y] == 0:
            idx += 1
            if idx == 10:
                break
        board1[x][y], board1[idx - 1][y] = board1[idx - 1][y], board1[x][y]
        board1[x + 1][y], board1[idx - 2][y] = board1[idx - 2][y], board1[x + 1][y]


        idx = 6
        while board2[idx][3 - x] == 0 and board2[idx][2 - x] == 0:
            idx += 1
            if idx == 10:
                break
        board2[y][3 - x], board2[idx - 1][3 - x] = board2[idx - 1][3 - x], board2[y][3 - x]
        board2[y][2 - x], board2[idx - 1][2 - x] = board2[idx - 1][2 - x], board2[y][2 - x]

    # 꽉찬 줄 있으면 우선 점수 처리
    checked = True
    while True:
        # 한 줄씩 체크하고 한 줄 지우면 다시 검사
        checked = check_row(board1)
        # 더 이상 꽉찬 줄 없으면 탈출
        if not checked:
            break
    while True:
        checked = check_row(board2)
        if not checked:
            break

    # 연한보드에 블록있으면 아래줄부터 제거
    remove_block(board1)
    remove_block(board2)

# 칸이 채워진 타일 수 계산
for i in range(6, 10):
    for j in range(4):
        if board1[i][j] == 1:
            block += 1
        if board2[i][j] == 1:
            block += 1

print(ans)
print(block)
