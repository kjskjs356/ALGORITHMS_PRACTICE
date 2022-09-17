# 17822 원판 돌리기

from collections import deque

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    stack.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny == -1: ny = M - 1
            if ny == M: ny = 0
            # 반지름 범위만 안벗어나는 지 확인
            if 0 <= nx <= N - 1 and not visited[nx][ny] and circle[x][y] == circle[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                stack.append((nx, ny))


# N : 반지름
# M : 원판에 있는 숫자갯수
# T : 회전 수
N, M, T = map(int, input().split())
circle = []
for i in range(N):
    circle.append(deque(list(map(int ,input().split()))))
x, d, k = [], [], []
result = 0
for _ in range(T):
    # x : 배수, d : 방향, k : 회전 칸 수
    a, b, c = map(int, input().split())
    x.append(a)
    d.append(b)
    k.append(c)

for i in range(T):
    flag = True
    # 회전 시행
    for j in range(N):
        # 배수 체크
        if (j + 1) % x[i] == 0:
            # 0이면 시계방향, 1이면 반시계방향 회전
            if d[i] == 0:
                circle[j].rotate(k[i])
            elif d[i] == 1:
                num = -k[i]
                circle[j].rotate(num)

    # 인접한 수 동일하면 제거
    visited = [[False] * M for _ in range(N)]
    for j in range(N):
        for l in range(M):
            stack = []
            if not visited[j][l] and circle[j][l] != 0:
                bfs(j, l)
            if len(stack) > 1:
                flag = False
                for a, b in stack:
                    circle[a][b] = 0

    # 인접한 경우가 아예 없는 경우 평균 계산해서 값 처리
    if flag:
        sum_circle = 0
        cnt = 0
        for j in range(N):
            for l in range(M):
                if circle[j][l] != 0:
                    sum_circle += circle[j][l]
                    cnt += 1
        if cnt > 0:
            avg = sum_circle / cnt
            for j in range(N):
                for l in range(M):
                    if circle[j][l] != 0:
                        if circle[j][l] > avg:
                            circle[j][l] -= 1
                        elif circle[j][l] < avg:
                            circle[j][l] += 1

for i in range(N):
    for j in range(M):
        result += circle[i][j]
print(result)
