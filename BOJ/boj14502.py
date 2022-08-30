# 14502 연구소 풀이

def dfs(x, y):
    global N, M
    # 범위 벗어나면 리턴
    if not (0 <= x <= N - 1 and 0 <= y <= M - 1):
        return
    else:
        # 빈 공간인 경우 바이러스 침투
        if field[x][y] == 0:
            field[x][y] = 2
            dfs(x, y + 1)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x - 1, y)
        else:
            return

# 벽 생성 함수
def create_wall(x, y):
    global wall, install_wall
    for i in range(x, N):
        for j in range(y, M):
            # wall 3 될때까지 빈공간에 벽 생성
            if field[i][j] == 0 and wall < 3:
                wall += 1
                field[i][j] = 1
                install_wall.append([i, j])
    print(install_wall)

# 설치했던 벽 초기화 함수
def init_field():
    global wall
    global install_wall
    for x, y in install_wall:
        field[x][y] = 0
    install_wall = []
    wall = 0

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
result = 0
wall = 0
install_wall = []
visited = [[False] * N for _ in range(M)]
# 0: 빈칸, 1: 벽, 2: 바이러스
for i in range(N):
    for j in range(M):
        create_wall(i, j)
        cnt = 0
        for k in range(N):
            print(field[k])
        print()
        # 연구소를 순회하면서 바이러스 위치 탐색
        for k in range(N):
            for l in range(M):
                if field[k][l] == 2:
                    dfs(k, l)
        # 안전 영역 넓이 계산
        for k in range(N):
            for l in range(M):
                if field[k][l] == 0:
                    cnt += 1
        if result < cnt:
            result = cnt
        init_field()
print(result)
