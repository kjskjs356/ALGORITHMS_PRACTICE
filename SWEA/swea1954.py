# 연습문제3_달팽이_숫자 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_map = [[0] * N for _ in range(N)]
    #델타 탐색
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0

    for i in range(N*N):
        num_map[x][y] = i + 1
        nx = x + dx[idx % 4]
        ny = y + dy[idx % 4]
        # 인덱스가 map 범위를 벗어나는지 & 다음 칸에 숫자가 0인지 아닌지 체크
        if (0 <= nx <= N - 1 and 0 <= ny <= N - 1) and num_map[nx][ny] == 0:
            x, y = nx, ny
        else:
            idx += 1
            x += dx[idx % 4]
            y += dy[idx % 4]
    print('#{}' .format(tc))
    for i in range(N):
        for j in range(N):
            print(num_map[i][j], end=' ')
        print()