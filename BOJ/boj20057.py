# 20057 마법사 상어와 토네이도


def sand_remain(x, y, sand):
    global result, remain
    # 남아 있는 모래의 양
    if not(0 <= x <= N - 1 and 0 <= y <= N - 1):
        result += sand - remain
    else:
        field[x][y] += sand - remain


def tornado(x, y, d, sand):
    global result, remain
    for dx, dy, percent in direction[d_list[d]]:
        if not (0 <= x + dx <= N - 1 and 0 <= y + dy <= N - 1):
            result += int(sand * percent)
        else:
            field[x + dx][y + dy] += int(sand * percent)
        remain += int(sand * percent)


d_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]

direction = {
    (0, -1): [[0, -2, 0.05], [-1, -1, 0.1], [1, -1, 0.1], [-1, 0, 0.07], [1, 0, 0.07],
              [-1, 1, 0.01], [1, 1, 0.01], [-2, 0, 0.02], [2, 0, 0.02]],
    (1, 0): [[2, 0, 0.05], [1, -1, 0.1], [1, 1, 0.1], [0, -1, 0.07], [0, 1, 0.07],
             [-1, -1, 0.01], [-1, 1, 0.01], [0, -2, 0.02], [0, 2, 0.02]],
    (0, 1): [[0, 2, 0.05], [1, 1, 0.1], [-1, 1, 0.1], [1, 0, 0.07], [-1, 0, 0.07],
             [1, -1, 0.01], [-1, -1, 0.01], [2, 0, 0.02], [-2, 0, 0.02]],
    (-1, 0): [[-2, 0, 0.05], [-1, 1, 0.1], [-1, -1, 0.1], [0, 1, 0.07], [0, -1, 0.07],
              [1, 1, 0.01], [1, -1, 0.01], [0, 2, 0.02], [0, -2, 0.02]],
}

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
x, y = N // 2, N // 2
result = 0
# 이동 거리
move = 1
# 방향 0:왼쪽, 1: 아래쪽, 2: 오른쪽, 3: 위쪽
d = 0
a, b = d_list[0]
while True:
    cnt = 0
    while cnt < 2:
        for i in range(move):
            if x == 0 and y == 0:
                break
            # 해당 방향으로 move 만큼 이동 후 회전
            dx, dy = d_list[d % 4]
            x += dx
            y += dy
            # 갱신된 좌표에서 토네이도 실행
            remain = 0
            tornado(x, y, d % 4, field[x][y])
            sand_remain(x + dx, y + dy, field[x][y])
            field[x][y] = 0
        d += 1
        cnt += 1
    move += 1
    if x == 0 and y == 0:
        break
print(result)
