# 2178 미로탐색

def bfs(x, y, cnt):
    visited[x][y] = True
    stack.append((x, y, cnt))
    while stack:
        x, y, cnt = stack.pop(0)
        if x == N - 1 and y == M - 1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다른 노드에서 먼저 도착한 값이 가장 작은 값이므로 이미 방문한 곳은 패스
            if (0 <= nx <= N - 1 and 0 <= ny <= M - 1)\
                    and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny, cnt + 1))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
stack = []
# 스타트 지점
x, y = 0, 0
# 방문 여부 체크
visited = [[False] * M for _ in range(N)]

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 1
field_cnt = [[0] * M for _ in range(N)]
visited[x][y] = True
print(bfs(x, y, cnt))
