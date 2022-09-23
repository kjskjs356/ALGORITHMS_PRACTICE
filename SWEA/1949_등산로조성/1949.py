# 1949_등산로 조성 풀이
# 2022-09-23

import sys
sys.stdin = open('input.txt', 'r')


def dfs():
    global K, result, cnt
    if result < cnt:
        result = cnt
        print(result)
        print()
    x, y, cut = stack[-1]
    print(field[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
            if not visited[nx][ny]:
                # 다음 칸의 높이가 더 높은 경우 높이를 깎을수 있다면 현재 높이 보다 최대한 적게 차이나도록 깎기
                if field[nx][ny] >= field[x][y]:
                    if cut == 0 and K > (field[nx][ny] - field[x][y]):
                        cut = 1
                        field[nx][ny] = field[x][y] - 1
                    else:
                        continue
                visited[nx][ny] = True
                stack.append((nx, ny, cut))
                cnt += 1
                dfs()
                cnt -= 1
                visited[nx][ny] = False
                stack.pop()
    if not stack:
        return

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    # K : 공사 가능 깊이
    N, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    result, cnt = 1, 1
    # 가장 높은 봉우리 탐색
    max_h = 0
    for i in range(N):
        for j in range(N):
            if max_h < field[i][j]:
                max_h = field[i][j]
    # 가장 높은 봉우리 에서만 확인
    for i in range(N):
        for j in range(N):
            if field[i][j] == max_h:
                stack = []
                stack.append((i, j, 0))
                visited = [[False] * N for _ in range(N)]
                visited[i][j] = True
                dfs()
    print('#{} {}' .format(tc, result))
    print()