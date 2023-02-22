# 17484 진우의 달 여행 (Small)

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
temp = 0

dx = [1, 1, 1]
dy = [-1, 0, 1]

# 지구부터 달까지 완탐
def back(x, y, cnt, v, last_direct):
    global ans
    if x == N - 1:
        if ans > cnt:
            ans = cnt
            return
    if ans < cnt:
        return
    for i in range(3):
        # 직전 방향과 일치하면 패스
        if last_direct == i:
            continue
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            # 방문 체크
            if not v[nx][ny]:
                v[nx][ny] = True
                back(nx, ny, cnt + board[nx][ny], v, i)
                v[nx][ny] = False

for i in range(M):
    # 연속 방향 방지용 함수
    visited = [[False for _ in range(M)] for _ in range(N)]
    last_direct = 4
    temp = board[0][i]
    back(0, i, temp, visited, last_direct)

print(ans)