# 17141 낚시왕

# 낚시왕이 잡은 상어 크기의 합 구하는 문제


def catch_shark(fish_man):
    for i in range(R):
        if len(board[i][fish_man]) > 0:
            cnt = board[i][fish_man][0][2]
            board[i][fish_man] = []
            return cnt
    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, M = map(int, input().split())
ans = 0
#상어 배치
board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    board[r][c].append([s, d, z, False])
fish_man = 0

while fish_man <= C - 1:
    board2 = [[[] for _ in range(C)] for _ in range(R)]
    # 상어 잡기
    sum_len = 0
    for i in range(R):
        sum_len += len(board[i][fish_man])
    if sum_len > 0:
        ans += catch_shark(fish_man)
    # 상어 이동
    for i in range(R):
        for j in range(C):
            if len(board[i][j]) > 0:
                # 아직 이동안한 상어만 이동
                for k in range(len(board[i][j])):
                    if not board[i][j][k][3]:
                        x, y = i, j
                        s, d, z, is_move = board[i][j][k][0], board[i][j][k][1], board[i][j][k][2], board[i][j][k][3]
                        is_move = True
                        # 반복 이동을 최소화시키기
                        if d <= 1:
                            s %= (R - 1) * 2
                        else:
                            s %= (C - 1) * 2
                        # 속력만큼 이동
                        for _ in range(s):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx <= R - 1 and 0 <= ny <= C - 1:
                                x, y = nx, ny
                            else:
                                if d in (0, 2):
                                    d += 1
                                elif d in (1, 3):
                                    d -= 1
                                x += dx[d]
                                y += dy[d]

                        # 이동 마치고 새 배열에 재배치
                        board2[x][y].append([s, d, z, is_move])

    # 이동 마친 후 가장 큰 상어만 생존
    for i in range(R):
        for j in range(C):
            if len(board2[i][j]) > 0:
                max_size = 0
                for k in range(len(board2[i][j])):
                    temp_size = board2[i][j][k][2]
                    if max_size < temp_size:
                        max_size = temp_size
                        info = [board2[i][j][k][0], board2[i][j][k][1], board2[i][j][k][2], False]
                # 가장 큰 상어의 정보만 남기기(이동여부 초기화)
                board2[i][j] = [info]
    # 원래 배열에 다시 복사
    board = [arr[:] for arr in board2]
    fish_man += 1
print(ans)