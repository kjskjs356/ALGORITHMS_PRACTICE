# 14500 테트로미노

# 'ㅗ'블록을 제외한 모든 블럭
def back(x, y, total, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            back(nx, ny, total + area[nx][ny], cnt + 1)
            visited[nx][ny] = False


def back2(x, y):
    global ans
    # 4방향 체크
    for i in range(4):
        temp = area[x][y]
        breaker = False
        # 각 방향마다 하나씩 제외해서 체크
        for j in range(4):
            if i == j: continue
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                temp += area[nx][ny]
            else:
                breaker = True
                break
        if breaker: continue
        ans = max(ans, temp)


N ,M = map(int, input().split())
area = [list(map(int, input().split()))for _ in range(N)]
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 0,0칸부터 완탐 시행
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        # 'ㅗ'를 제외한 블럭 체크
        back(i, j, area[i][j], 1)
        visited[i][j] = False
        # 'ㅗ'블럭 체크 (4꼭짓점은 제외)
        if i != 0 and j != 0 or i != 0 and j != M - 1 or i != N - 1 and j != 0 or i != N - 1 and j != M - 1:
            back2(i, j)
print(ans)