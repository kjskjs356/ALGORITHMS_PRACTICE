# 1913 달팽이

N = int(input())
K = int(input())

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
field = [[0] * N for _ in range(N)]
x, y, i = 0, 0, 0
num = N**2
field[x][y] = num
if num == K:
    result_x, result_y = x + 1, y + 1
#제일 큰 수부터 역순
while True:
    nx = x + dx[i % 4]
    ny = y + dy[i % 4]
    # 범위 벗어나거나 이미 숫자 할당된 배열이면 방향 전환
    if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1) or field[nx][ny] != 0:
        i += 1
        continue
    else:
        num -= 1
        field[nx][ny] = num
        # 타겟 숫자인 경우 좌표 기록
        if num == K:
            result_x, result_y = nx + 1, ny + 1
        x, y = nx, ny
        if num == 1:
            break
for i in range(N):
    print(*field[i])
print(result_x, result_y)