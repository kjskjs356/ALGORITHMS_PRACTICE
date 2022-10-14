# 청소년 상어 풀이

"""
물고기 번호 : 1 ~ 16 모두 고유 번호
상어가 먹은 물고기 번호 최대값을 구하려면 가능한 경우의 수 모두 탐색
백트래킹 사용
상어가 먹은 물고기 번호를 리스트로 만들어서 방문 여부로 체크
"""


#물고기 복귀함수



# 물고기 이동함수
def fish_move(arr):
    # 낮은 번호의 물고기부터 이동
    for num in range(1, 17):
        if not fish_list[num]:
            continue
        is_move = False
        for x in range(4):
            if is_move:
                break
            for y in range(4):
                if is_move:
                    break
                if arr[x][y][0] == num:
                    for i in range(8):
                        nx = x + dx[(arr[x][y][1] + i - 1) % 8]
                        ny = y + dy[(arr[x][y][1] + i - 1) % 8]
                        # 상어가 있거나 벗어나는 칸이 아니면 이동
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if not (shark_x == nx and shark_y == ny):
                                arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                                is_move = True
                                break
    return arr


def back(x, y, d, idx, tmp):
    global ans
    if not (0 <= x < 4 and 0 <= y < 4):
        return
    if tmp > ans:
        ans = tmp


# 12시 부터 반시계방향 (8방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
visited = [[False] * 4 for _ in range(4)]
fish_list = [True for _ in range(17)]
area = [[[0, 0] for _ in range(4)] for _ in range(4)]
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        area[i][j][0] = arr[2 * j]
        area[i][j][1] = arr[2 * j + 1]

# 최초 상어 (0, 0) 투입
shark_x, shark_y = 0, 0
ans = area[0][0][0]
shark_direct = area[0][0][1] - 1
fish_list[area[0][0][0]] = False

for i in range(4):
    print(area[i])
print()

# 물고기 이동
area = fish_move(area)
idx = 0

for i in range(4):
    print(area[i])
print()

back(0, 0, shark_direct, idx, ans)