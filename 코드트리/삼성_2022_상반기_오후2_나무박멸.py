import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 상반기 오후 2번 나무박멸

n, m, k, c = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
killTree = [[0] * n for _ in range(n)]
ans = 0

# 성장 및 번식용 델타탐색
dx1 = [1, -1, 0, 0]
dy1 = [0, 0, 1, -1]

# 제초용 대각선방향 델타탐색
dx2 = [1, 1, -1, -1]
dy2 = [1, -1, 1, -1]

for _ in range(m):
    # 0. 제초구역 -1씩 하기
    for x in range(n):
        for y in range(n):
            if killTree[x][y] > 0:
                killTree[x][y] -= 1

    # 1. 인접한 나무의 수만큼 해당 칸 나무 성장. 단, 제초제가 뿌려진 나무는 제외
    for x in range(n):
        for y in range(n):
            # 제초된 나무와 빈칸은 패스
            if killTree[x][y] == 0 and tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] > 0:
                        cnt += 1
                tree[x][y] += cnt

    # 2. 번식가능한 칸으로 나무 번식(벽, 제초구역, 다른나무 있는 구역 불가능)
    tree2 = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                num = tree[x][y]
                cnt = 0
                # 번식 가능한 구역의 개수 설정
                for i in range(4):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] == 0 and killTree[nx][ny] == 0:
                        cnt += 1
                if cnt == 0: continue
                share = num // cnt
                # 번식 가능한 구역에 번식 실행
                for i in range(4):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] == 0 and killTree[nx][ny] == 0:
                        tree2[nx][ny] += share
    # 번식 끝난 후 맵 동기화
    for x in range(n):
        for y in range(n):
            if tree2[x][y] > 0:
                tree[x][y] = tree2[x][y]

    # 제초작업 실행, 각 나무를 탐색하여 가장 많이 박멸가능한 칸 탐색
    tx, ty, maxKill = -1, -1, 0
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                tempMax = tree[x][y]
                for i in range(4):
                    for cnt in range(1, k + 1):
                        nx = x + dx2[i] * cnt
                        ny = y + dy2[i] * cnt
                        if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] > 0:
                            tempMax += tree[nx][ny]
                        else: break
                # 가장 많이 박멸한 경우 해당 좌표와 값 기록
                if tempMax > maxKill:
                    tx, ty, maxKill = x, y, tempMax
    # 가장 많이 박멸가능한 칸에서 제초 실행
    for i in range(4):
        for cnt in range(1, k + 1):
            nx = tx + dx2[i] * cnt
            ny = ty + dy2[i] * cnt
            if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] > 0:
                tree[nx][ny] = 0
                killTree[nx][ny] = c + 1
            elif 0 <= nx < n and 0 <= ny < n and tree[nx][ny] == 0:
                killTree[nx][ny] = c + 1
                break
            else: break
    tree[tx][ty] = 0
    killTree[tx][ty] = c + 1
    ans += maxKill

print(ans)