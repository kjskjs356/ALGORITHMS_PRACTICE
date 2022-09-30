# 빵집 풀이

def dfs(x, y):
    global flag
    if flag:
        return
    # 끝에 도달
    if y == C - 1:
        flag = True
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if area[nx][ny] != 'x' and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)
                if flag:
                    return


# 우상, 우, 우하
dx = [-1, 0, 1]
dy = [1, 1, 1]

R, C = map(int, input().split())
area = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0
# 첫 번째 열부터 마지막 열까지 진행
for idx in range(R):
    x, y = idx, 0
    if area[x][y] == 'x':
        continue
    flag = False
    visited[x][y] = True
    dfs(x, y)
    if flag:
        ans += 1
print(ans)
