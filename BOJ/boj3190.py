# 3190_뱀 풀이

# 우 하 좌 상 => 1 증가할 때마다 시계방향 90도
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
d = 0
i = 0
N = int(input())
board = [[False] * N for _ in range(N)]
board[0][0] =  True
K = int(input())
apple = []
head_x, head_y = 0, 0
tale_x, tale_y = 0, 0
time, length = 0, 1
breaker = False

# 사과 생성
for _ in range(K):
    apple_x, apple_y = map(int, input().split())
    apple.append([apple_x - 1, apple_y - 1])

# 뱀의 움직임 생성
move = []
L = int(input())
for _ in range(L):
    moving, direct = map(str, input().split())
    move.append([int(moving), direct])

# 완주 or 게임오버 까지 반복
while True:
    if breaker:
        break
    if i >= L:
        while True:
            time += 1
            nx = x + dx[d % 4]
            ny = y + dy[d % 4]
            print(nx, ny)
            # 벽에 닿으면 종료
            if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
                breaker = True
                break
            # 꼬리에 닿으면 종료
            elif board[nx][ny]:
                breaker = True
                break
            # 사과 먹었으면 사과 없애고 꼬리변화 X
            if [nx, ny] in apple:
                apple.remove([nx, ny])
                board[nx][ny] = True
                head_x, head_y = nx, ny
                x, y = nx, ny
                length += 1
            # 사과 안먹었으면 꼬리 축소
            else:
                board[nx][ny] = True
                head_x, head_y = nx, ny
                board[tale_x][tale_y] = False
                x, y = nx, ny
                # 다음 꼬리 탐색
                for j in range(4):
                    if 0 <= tale_x + dx[j] <= N - 1 and 0 <= tale_y + dy[j] <= N - 1:
                        if board[tale_x + dx[j]][tale_y + dy[j]]:
                            if tale_x + dx[j] == head_x and tale_y + dy[j] == head_y:
                                if length == 1:
                                    tale_x += dx[j]
                                    tale_y += dy[j]
                                else:
                                    continue
                            else:
                                tale_x += dx[j]
                                tale_y += dy[j]
                    else:
                        continue
    else:
        while time < move[i][0]:
            time += 1
            nx = x + dx[d % 4]
            ny = y + dy[d % 4]
            print(nx, ny)
            # 벽에 닿으면 종료
            if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
                breaker = True
                break
            #꼬리에 닿으면 종료
            elif board[nx][ny]:
                breaker = True
                break
            #사과 먹었으면 꼬리변화 X
            if [nx, ny] in apple:
                apple.remove([nx, ny])
                board[nx][ny] = True
                head_x, head_y = nx, ny
                x, y = nx, ny
                length += 1
            #사과 안먹었으면 꼬리 축소
            else:
                board[nx][ny] = True
                head_x, head_y = nx, ny
                board[tale_x][tale_y] = False
                x, y = nx, ny
                #다음 꼬리 탐색
                for j in range(4):
                    if 0 <= tale_x + dx[j] <= N - 1 and 0 <= tale_y + dy[j] <= N - 1:
                        if board[tale_x + dx[j]][tale_y + dy[j]]:
                            if tale_x + dx[j] == head_x and tale_y + dy[j] == head_y:
                                if length == 1:
                                    tale_x += dx[j]
                                    tale_y += dy[j]
                                else:
                                    continue
                            else:
                                tale_x += dx[j]
                                tale_y += dy[j]
                    else:
                        continue
        if move[i][1] == 'L':
            d += 3
        elif move[i][1] == 'D':
            d += 1
    i += 1
print(time)