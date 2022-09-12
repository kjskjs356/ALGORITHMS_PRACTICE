# 16234 인구 이동

from collections import deque

N, L, R = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
tmp = 0
cnt = 0
day = 0

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 인구 이동 함수
def move():
    global tmp, cnt
    result = tmp // cnt
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                field[i][j] = result
                check[i][j] = 2

# 국경 오픈 함수
def aliance(x, y):
    global tmp, cnt
    q.append([x, y])
    check[x][y] = 1
    while q:
        a, b = q.popleft()
        tmp += field[a][b]
        cnt += 1
        for i in range(4):
            if 0 <= a + dx[i] <= N - 1 and 0 <= b + dy[i] <= N - 1:
                # 조건 충족하면 국경 오픈
                if (L <= abs(field[a][b] - field[a + dx[i]][b + dy[i]]) <= R) and check[a + dx[i]][b + dy[i]] == 0:
                    check[a + dx[i]][b + dy[i]] = 1
                    q.append([a + dx[i], b + dy[i]])
    # check[x][y] = 1
    # for i in range(4):
    #     if 0 <= x + dx[i] <= N - 1 and 0 <= y + dy[i] <= N - 1:
    #         # 조건 충족하면 국경 오픈
    #         if (L <= abs(field[x][y] - field[x + dx[i]][y + dy[i]]) <= R) and check[x + dx[i]][y + dy[i]] == 0:
    #             aliance(x + dx[i], y + dy[i])

# 인구 이동 끝날때까지 반복
q = deque()
while True:
    flag = True
    # 연합 구분용 배열 변수
    check = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 아직 체크 안되어있으면 연합 가능여부 확인
            if check[i][j] == 0:
                # 절대 값 비교로 국경오픈 시행
                aliance(i, j)
                # 연합이 2개 이상 이루어졌을 경우 국경 오픈된 나라 우선 인구 이동 시행
                print(tmp, cnt)
                if cnt > 1:
                    flag = False
                    move()
                else:
                    check[i][j] = 2
                tmp, cnt = 0, 0
                for i in range(N):
                    print(field[i])
                print()
                for i in range(N):
                    print(check[i])
                print()
    # 인구 이동 끝나면 연합 구분 초기화
    for i in range(N):
        for j in range(N):
            check[i][j] = 0
    if flag:
        break
    day += 1
print(day)