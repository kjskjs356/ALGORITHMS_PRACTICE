# 10157 자리배정

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가로: C, 세로: R
C, R = map(int, input().split())
K = int(input())
board = [[0] * C for _ in range(R)]
x, y = R - 1, 0
if C * R < K:
    print(0)
else:
    board[x][y] = 1
    if K == 1:
        print(y + 1, R - x)
    else:
        n = 2
        i = 0
        while n <= C * R:
            nx, ny = x + dx[i % 4], y + dy[i % 4]
            if 0 <= nx <= R - 1 and 0 <= ny <= C - 1:
                if board[nx][ny] == 0:
                    board[nx][ny] = n
                    x, y = nx, ny
                    if n == K:
                        break
                    n += 1
                else:
                    i += 1
            else:
                i += 1
        print(ny + 1, R - nx)