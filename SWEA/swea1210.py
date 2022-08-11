# 1210 Ladder1 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')
#    좌 우 상
dx = [-1, 1, 0]
dy = [0, 0, -1]

for tc in range(1, 11):
    tc_num = int(input())
    data = []
    result = 0
    for i in range(100):
        data.append(list(map(int, input().split())))
    # 마지막 줄 부터 시작
    for i in range(100):
        if data[99][i] == 2:
            x, y = i, 99
    j = 2
    while True:
        while j == 0:
            # 왼쪽 여부
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx <= 99:
                if data[ny][nx]:
                    x, y = nx, ny
                else:
                    j = 2; break
            else:
                j = 2; break
        while j == 1:
            # 오른쪽 여부
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx <= 99:
                if data[ny][nx]:
                    x, y = nx, ny
                else:
                    j = 2; break
            else:
                j = 2; break
        while j == 2:
            # 직진 여부
            nx = x + dx[j]
            ny = y + dy[j]
            if y == 0:
                break
            if 0 <= nx - 1 <= 99 and data[ny][nx - 1] == 1:
                x, y = nx, ny
                j = 0
            elif 0 <= nx + 1 <= 99 and data[ny][nx + 1] == 1:
                x, y = nx, ny
                j = 1
            else:
                x, y = nx, ny
        if y == 0:
            break
    print('#{} {}'. format(tc, x))