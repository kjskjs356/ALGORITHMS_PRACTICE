# 16235 나무 제테크

# 8방향 (12시부터)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

# K 년간 반복
for _ in range(K):
    # 봄 => 각 나무가 자신의 나이만큼 양분 섭취, 부족하면 나무 죽고 양분이됨
    for i in range(N):
        for j in range(N):
            temp = 0
            is_end = True
            if len(tree[i][j]) == 0:
                continue
            # 나이 어린순으로 정렬
            tree[i][j].sort()
            for k in range(len(tree[i][j])):
                # 충분한 양분이 있으면 양분주입 & 나무 성장
                if board[i][j] >= tree[i][j][k]:
                    board[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    temp += int(tree[i][j][k] / 2)
                    if is_end:
                        end = k
                        is_end = False
            if is_end:
                end = len(tree[i][j])
            # 여름 => 양분을 먹지못한 나무까지는 제외하고 죽음(슬라이싱)
            board[i][j] += temp
            tree[i][j] = tree[i][j][:end]

    # 가을 => 나이 5의 배수 나무 번식
    for x in range(N):
        for y in range(N):
            if len(tree[x][y]) == 0:
                continue
            for k in range(len(tree[x][y])):
                # 나무 번식 가능 유무 판단
                if tree[x][y][k] % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].append(1)
    #  겨울 => 양분 주입
    board = [[a + b for a, b in zip(x, y)] for x, y in zip(nutrient, board)]
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)