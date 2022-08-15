# 3190_뱀 풀이

# 우 하 좌 상 => 1 증가할 때마다 시계방향 90도
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
d = 0
i = 0
N = int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = 3
K = int(input())
apple = []
d_map = [['.'] * N for _ in range(N)]
tale_x, tale_y = 0, 0
last_d = 'D'
tale_direct = []
time, length = 0, 1
breaker = False

# 사과 생성
for _ in range(K):
    a_x, a_y = map(int, input().split())
    board[a_x - 1][a_y - 1] = 1

# 뱀의 움직임 생성
move = []
L = int(input())
for _ in range(L):
    moving, direct = map(str, input().split())
    move.append([int(moving), direct])
# 게임 시작
while True:
    if i == L:
        while True:
            time += 1
            d_map[x][y] = last_d
            nx = x + dx[d % 4]
            ny = y + dy[d % 4]
            # 벽에 닿으면 종료
            if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
                breaker = True
                break
            # 꼬리에 닿으면 종료
            elif board[nx][ny] == 2:
                breaker = True
                break
            # 사과 먹었으면 꼬리변화 X
            if board[nx][ny] == 1:
                board[nx][ny] = 3
                board[x][y] = 2
                tale_direct.append(d % 4)
                x, y = nx, ny
                length += 1
            # 사과 안먹었으면 꼬리 축소
            else:
                board[nx][ny] = 3
                board[x][y] = 2
                tale_direct.append(d % 4)
                board[tale_x][tale_y] = 0
                x, y = nx, ny
                # 다음 꼬리 탐색
                tale_x += dx[tale_direct[0]]
                tale_y += dy[tale_direct[0]]
                tale_direct.pop(0)
        if breaker:
            break

    else:
        while time < move[i][0]:
            time += 1
            d_map[x][y] = move[i][1]
            nx = x + dx[d % 4]
            ny = y + dy[d % 4]
            # 벽에 닿으면 종료
            if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
                breaker = True
                break
            #꼬리에 닿으면 종료
            elif board[nx][ny] == 2:
                breaker = True
                break
            #사과 먹었으면 꼬리변화 X
            if board[nx][ny] == 1:
                board[nx][ny] = 3
                board[x][y] = 2
                tale_direct.append(d % 4)
                x, y = nx, ny
                length += 1
            #사과 안먹었으면 꼬리 축소
            else:
                board[nx][ny] = 3
                board[x][y] = 2
                tale_direct.append(d % 4)
                board[tale_x][tale_y] = 0
                x, y = nx, ny
                #다음 꼬리 탐색
                tale_x += dx[tale_direct[0]]
                tale_y += dy[tale_direct[0]]
                tale_direct.pop(0)
        if breaker:
            break
        if move[i][1] == 'L':
            last_d = 'L'
            d += 3
        elif move[i][1] == 'D':
            last_d = 'D'
            d += 1
        i += 1
print(time)