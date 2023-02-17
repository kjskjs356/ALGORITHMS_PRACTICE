from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 장마에 잠기는 영역
def rain(n):
    for i in range(N):
        for j in range(N):
            if board[i][j] <= n:
                save[i][j] = False


#안전구역 계산
def save_area(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if save[nx][ny]:
                    save[nx][ny] = False
                    q.append((nx, ny))


N = int(input())
total_max = 0
board = []
#최대 구역
max_cnt = 0
# 영역 설정하면서 min값 ,max값 찾기
for _ in range(N):
    arr = list(map(int, input().split()))
    temp_max = max(arr)
    if total_max < temp_max:
        total_max = temp_max
    board.append(arr)

for i in range(total_max):
    temp_cnt = 0
    save = [[True] * N for _ in range(N)]
    # 장마로 인해 최소높이부터 물에 잠기기
    rain(i)
    #안전 구역 계산(잠긴 곳은 패스)
    for j in range(N):
        for k in range(N):
            if save[j][k]:
                save[j][k] = False
                save_area(j, k)
                temp_cnt += 1
    if max_cnt < temp_cnt:
        max_cnt = temp_cnt
if max_cnt == 0:
    max_cnt += 1
print(max_cnt)