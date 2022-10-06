# 마법사 상어와 비바라기 풀이

def new_cloud(v):
    for i in range(N):
        for j in range(N):
            if area[i][j] >= 2 and not v[i][j]:
                area[i][j] -= 2
                v[i][j] = True
            elif v[i][j]:
                v[i][j] = False


def raise_water(v):
    for i in range(N):
        for j in range(N):
            if v[i][j]:
                # 대각선 4방향 체크
                for k in range(4):
                    ni = i + dxx[k]
                    nj = j + dyy[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if area[ni][nj] > 0:
                            area[i][j] += 1


def rain():
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                area[i][j] += 1


def cloud_move(d, s):
    new_v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                ni = (i + dx[d] * s) % N
                nj = (j + dy[d] * s) % N
                new_v[ni][nj] = visited[i][j]
    return new_v


# 9시 방향부터 시계방향(총 8방향)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 4방향 델타탐색
dxx = [-1, -1, 1, 1]
dyy = [-1, 1, 1, -1]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 최초 구름 생성
visited = [[False] * N for _ in range(N)]
visited[N - 2][0], visited[N - 1][0], visited[N - 2][1], visited[N - 1][1] = True, True, True, True
for n in range(M):
    d, s = map(int, input().split())
    d -= 1
    visited = cloud_move(d, s)
    # True인 곳 비 1씩 내림
    rain()
    # 대각선 방향 물 체크 후 물 양 증가
    raise_water(visited)
    # 기존 구름 제거 & 새로운 구름 생성 후 물 양 2 감소
    new_cloud(visited)
for i in range(N):
    ans += sum(area[i])
print(ans)