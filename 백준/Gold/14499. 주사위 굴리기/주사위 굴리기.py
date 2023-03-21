# 14499 주사위 굴리기


def move(d):
    # 동쪽
    if d == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = \
            dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    # 서쪽
    elif d == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = \
            dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    # 북쪽
    elif d == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = \
            dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
    # 남쪽
    elif d == 4:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = \
            dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]

N, M, x, y, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 인덱스 => 1: 위, 2: 뒤, 3: 오른, 4: 왼, 5: 앞, 6: 아래
dice = [0] * 7
for i in command:
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
        move(i)
        # 지도 칸이 0이면 주사위에서 지도로 복사
        if area[nx][ny] == 0:
            area[nx][ny] = dice[6]
        # 지도 칸이 0이 아니면 주사위로 숫자이동, 지도는 0
        else:
            dice[6] = area[nx][ny]
            area[nx][ny] = 0
        print(dice[1])
        x, y = nx, ny