# 스타트 택시 풀이

from collections import deque


def bfs(a, b):
    q = deque()
    tmp_visited = [[0] * N for _ in range(N)]
    q.append((a, b))
    tmp_visited[a][b] = 0
    min_distance = float('inf')
    arr = []
    while q:
        x, y = q.popleft()
        if tmp_visited[x][y] > min_distance:
            break
        if [x, y] in taxi_start:
            min_distance = tmp_visited[x][y]
            arr.append([x, y])
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if area[nx][ny] == 0 and tmp_visited[nx][ny] == 0:
                        tmp_visited[nx][ny] = tmp_visited[x][y] + 1
                        q.append((nx, ny))
    if arr:
        arr.sort()
        return tmp_visited[arr[0][0]][arr[0][1]], arr[0][0], arr[0][1]
    else:
        return -1, -1, -1


def bfs2(a, b, end_x, end_y):
    q = deque()
    tmp_visited = [[0] * N for _ in range(N)]
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if area[nx][ny] == 0 and tmp_visited[nx][ny] == 0:
                        tmp_visited[nx][ny] = tmp_visited[x][y] + 1
                        q.append((nx, ny))
    return tmp_visited[x][y],x, y


# def bfs2(a, b, end_x, end_y):
#     cnt = 0
#     q = deque()
#     tmp_visited = [[False] * N for _ in range(N)]
#     q.append((a, b, cnt))
#     while q:
#         x, y, cnt = q.popleft()
#         if x == end_x and y == end_y:
#             return cnt, True
#         if cnt > K:
#             return cnt, False
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if area[nx][ny] != 1 and not tmp_visited[nx][ny]:
#                     tmp_visited[nx][ny] = True
#                     q.append((nx, ny, cnt + 1))
#     return cnt, False


#우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            area[i][j] = -1
detiny = [[0] * N for _ in range(N)]
x, y = map(int, input().split())
x -= 1
y -= 1
taxi_start = []
taxi_end = []
# 방문한 승객 확인용 배열
for i in range(1, M + 1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    taxi_start.append([a, b])
    taxi_end.append([c, d])
ans = 0
# 가장 최단거리인 승객부터 탑승
for _ in range(M):
    start_distance, x, y = bfs(x, y)
    # 연료 부족하면 중단
    K -= start_distance
    if K <= 0 or start_distance == -1:
        ans = -1
        break
    idx = taxi_start.index([x, y])
    taxi_start[idx] = [-1, -1]
    # 승객 탑승후 목적지 까지 도착
    destiny_distance, x, y = bfs2(x, y, taxi_end[idx][0], taxi_end[idx][1])
    if not (x == taxi_end[idx][0] and y == taxi_end[idx][1]):
        ans = -1
        break
    K -= destiny_distance
    # 연료가 부족일 경우 중단
    if K < 0:
        ans = -1
        break
    K += destiny_distance * 2
    ans = K
print(ans)