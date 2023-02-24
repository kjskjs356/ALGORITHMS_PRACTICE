# 17837 새로운 게임2

# 이동 방향 [우, 하, 좌, 상]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, K = map(int, input().split())
horse = []

chess_map = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
ans = 0

for i in range(K):
    x, y, move = map(int, input().split())
    if move == 1:
        move = 0
    elif move == 2:
        move = 2
    elif move == 3:
        move = 3
    elif move == 4:
        move = 1
    horse.append([x - 1, y - 1, move])
    board[x - 1][y - 1].append(i + 1)

breaker = False
# 1번 말부터 이동
while True:
    ans += 1
    if ans > 1000:
        break
    for i in range(K):
        x, y = horse[i][0], horse[i][1]
        nx = x + dx[horse[i][2] % 4]
        ny = y + dy[horse[i][2] % 4]

        # 이동하려는 칸 범위 밖 or 파란색
        if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1) or chess_map[nx][ny] == 2:
            horse[i][2] += 2
            nx2 = x + dx[horse[i][2] % 4]
            ny2 = y + dy[horse[i][2] % 4]

            # 방향 바꾼 후
            # 이동하려는 칸 범위 밖 or 파란색
            if not (0 <= nx2 <= N - 1 and 0 <= ny2 <= N - 1) or chess_map[nx2][ny2] == 2:
                continue
            # 이동하려는 칸 흰색
            elif chess_map[nx2][ny2] == 0:
                idx = board[x][y].index(i + 1)
                end = len(board[x][y])
                arr = board[x][y][idx:end]
                board[nx2][ny2].extend(arr)
                board[x][y] = board[x][y][:idx]
            # 이동하려는 칸 빨간색
            elif chess_map[nx2][ny2] == 1:
                idx = board[x][y].index(i + 1)
                end = len(board[x][y])
                arr = board[x][y][idx:end]
                arr = arr[::-1]
                board[nx2][ny2].extend(arr)
                board[x][y] = board[x][y][:idx]

        # 이동하려는 칸 범위 안
        else:
            # 이동하려는 칸 흰색
            if chess_map[nx][ny] == 0:
                idx = board[x][y].index(i + 1)
                end = len(board[x][y])
                arr = board[x][y][idx:end]
                board[nx][ny].extend(arr)
                board[x][y] = board[x][y][:idx]
            # 이동하려는 칸 빨간색
            elif chess_map[nx][ny] == 1:
                idx = board[x][y].index(i + 1)
                end = len(board[x][y])
                arr = board[x][y][idx:end]
                arr = arr[::-1]
                board[nx][ny].extend(arr)
                board[x][y] = board[x][y][:idx]

        #위치 정보 갱신
        for j in range(N):
            for k in range(N):
                for l in range(1, K + 1):
                    if l in board[j][k]:
                        horse[l - 1][0], horse[l - 1][1] = j, k

        # 말이 4개인 칸이 생기면 종료
        for j in range(N):
            for k in range(N):
                if len(board[j][k]) >= 4:
                    breaker = True

        if breaker:
            break
    if breaker:
        break

if ans > 1000:
    print(-1)
else:
    print(ans)