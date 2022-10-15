# 청소년 상어 풀이

"""
물고기 번호 : 1 ~ 16 모두 고유 번호
상어가 먹은 물고기 번호 최대값을 구하려면 가능한 경우의 수 모두 탐색
백트래킹 사용
상어가 먹은 물고기 번호를 리스트로 만들어서 방문 여부로 체크
"""


# 물고기 이동함수
def fish_move(arr_num, arr_direct):
    # 낮은 번호의 물고기부터 이동
    for num in range(1, 17):
        is_move = False
        for x in range(4):
            if is_move:
                break
            for y in range(4):
                if is_move:
                    break
                if arr_num[x][y] == num:
                    while True:
                        nx = x + dx[(arr_direct[x][y] - 1) % 8]
                        ny = y + dy[(arr_direct[x][y] - 1) % 8]
                        # 상어가 있거나 벗어나는 칸이 아니면 이동
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if arr_num[nx][ny] >= 0:
                                arr_num[x][y], arr_num[nx][ny] = arr_num[nx][ny], arr_num[x][y]
                                arr_direct[x][y], arr_direct[nx][ny] = arr_direct[nx][ny], arr_direct[x][y]
                                is_move = True
                                break
                            else:
                                arr_direct[x][y] += 1
                                if arr_direct[x][y] > 8:
                                    arr_direct[x][y] = 1
                        else:
                            arr_direct[x][y] += 1
                            if arr_direct[x][y] > 8:
                                arr_direct[x][y] = 1


def back(x, y, d, tmp, area_num, area_direct):
    global ans
    if not (0 <= x < 4 and 0 <= y < 4):
        return
    if tmp > ans:
        ans = tmp
    fish_move(area_num, area_direct)
    for i in range(1, 4):
        nx = x + dx[d - 1] * i
        ny = y + dy[d - 1] * i
        # 상어 이동 탐색
        if 0 <= nx < 4 and 0 <= ny < 4:
            if area_num[nx][ny] > 0:
                num = area_num[nx][ny]
                direct = area_direct[nx][ny]
                area_num[x][y] = 0
                tmp += num
                area_num[nx][ny] = -1
                back(nx, ny, direct, tmp, [arr[:] for arr in area_num], [arr2[:] for arr2 in area_direct])
                tmp -= num
                area_num[x][y] = -1
                area_num[nx][ny] = num



# 12시 부터 반시계방향 (8방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
fish_num = [[0] * 4 for _ in range(4)]
fish_direct = [[0] * 4 for _ in range(4)]

for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        fish_num[i][j] = arr[2 * j]
        fish_direct[i][j] = arr[2 * j + 1]

# 최초 상어 (0, 0) 투입
shark_x, shark_y = 0, 0
ans = fish_num[0][0]
shark_direct = fish_direct[0][0]
fish_num[0][0] = -1
fish_direct[0][0] = 0

# 상어 이동 & 물고기 이동 반복
back(0, 0, shark_direct, ans, [arr[:] for arr in fish_num], [arr[:] for arr in fish_direct])
print(ans)