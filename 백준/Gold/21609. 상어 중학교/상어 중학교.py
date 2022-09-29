# 상어중학교 풀이

from collections import deque

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 그룹 체크용 bfs
def bfs(a, b, num):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    cnt = 1
    rainbow = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                # 동일한 색상이거나 무지개색일 경우 그룹으로 판단
                if (area[nx][ny] == num or area[nx][ny] == 0) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
                    if area[nx][ny] == 0:
                        rainbow += 1
    return cnt, rainbow


#그룹 제거용 bfs
def bfs2(a, b, num):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    area[a][b] = -2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                # bfs에서처럼 똑같이 탐색 후 역으로 요소 제거
                if (area[nx][ny] == num or area[nx][ny] == 0) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    area[nx][ny] = -2
                    q.append((nx, ny))


def rotate(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[N - j - 1][i] = arr[i][j]
    return new_arr


def ground():
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(area[j][i])
        flag = True
        # 중력이 더이상 작용안할때까지 반복
        while flag:
            flag = False
            for j in range(N - 2, -1, -1):
                if tmp[j] >= 0 and tmp[j + 1] == -2:
                    tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                    # 중력이 작용했으므로 True
                    flag = True
        # 중력 작용 끝나면 배열 복사
        for j in range(N):
            area[j][i] = tmp[j]


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 0 : 무지개 블록, -1 : 검은 블록, 그 외: 일반 블록
# 블록 탐색
while True:
    visited = [[False] * N for _ in range(N)]
    arr = []
    for i in range(N):
        for j in range(N):
            if area[i][j] > 0 and not visited[i][j]:
                # cnt : 크기, rainbow : 무지개 블록 수
                cnt, rainbow = bfs(i, j, area[i][j])
                arr.append((cnt, rainbow, i, j))
                # 무지개블록만 방문 초기화
                for k in range(N):
                    for l in range(N):
                        if area[k][l] == 0:
                            visited[k][l] = False
    # 1순위 : 큰 블록그룹, 2순위 : 무지개블록 수, 3순위 : 가장 빠른 행, 4순위 : 가장 빠른 열로 정렬
    arr.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    if not arr:
        break
    if arr[0][0] < 2:
        break
    # 큰 블록 제거 & 점수 획득
    ans += arr[0][0]**2
    visited = [[False] * N for _ in range(N)]
    bfs2(arr[0][2], arr[0][3], area[arr[0][2]][arr[0][3]])
    # 중력 작용
    ground()
    # 배열 회전
    area = rotate(area)
    # 중력 한번 더 작용
    ground()
    # 만약 빈공간만 남았을 경우 종료
    is_blank = True
    for i in range(N):
        for j in range(N):
            if area[i][j] != -2:
                is_blank = False
    if is_blank:
        break
print(ans)
