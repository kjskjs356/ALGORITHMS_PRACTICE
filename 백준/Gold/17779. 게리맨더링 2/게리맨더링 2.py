# 17779 게리맨더링2


# 중복 조합
def comb(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for j in comb(arr, n - 1):
                yield [arr[i]] + j


# 선거구 계산
def calculate(n, arr, v, x, y, d1, d2):
    # 구역 번호 별로 계산
    if n == 1:
        for i in range(x + d1):
            for j in range(y + 1):
                if bound[i][j] == 1:
                    break
                arr[n] += board[i][j]
                v[i][j] = True
    elif n == 2:
        for i in range(x + d2 + 1):
            for j in range(N - 1, y, -1):
                if bound[i][j] == 1:
                    break
                arr[n] += board[i][j]
                v[i][j] = True
    elif n == 3:
        for i in range(x + d1, N):
            for j in range(y - d1 + d2):
                if bound[i][j] == 1:
                    break
                arr[n] += board[i][j]
                v[i][j] = True
    elif n == 4:
        for i in range(x + d2 + 1, N):
            for j in range(N - 1, y - d1 + d2 - 1, -1):
                if bound[i][j] == 1:
                    break
                arr[n] += board[i][j]
                v[i][j] = True
    elif n == 5:
        for i in range(N):
            for j in range(N):
                if not v[i][j]:
                    v[i][j] = True
                    arr[n] += board[i][j]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

# 각 칸을 기준점으로 완탐 시행
for x in range(N - 2):
    for y in range(1, N - 1):
        for arr in comb(list(range(1, N)), 2):
            area = [0 for _ in range(6)]
            visited = [[False for _ in range(N)] for _ in range(N)]
            bound = [[0 for _ in range(N)] for _ in range(N)]
            bound[x][y] = 1
            max_d1, max_d2 = arr[0], arr[1]
            if 0 <= x + max_d1 + max_d2 <= N - 1 and 0 <= y - max_d1 and y + max_d2 <= N - 1:
                d1, d2 = 0, 0
                while True:
                    if d1 < max_d1:
                        d1 += 1
                    if d2 < max_d2:
                        d2 += 1
                    bound[x + d1][y - d1] = 1
                    bound[x + d2][y + d2] = 1
                    if d1 >= max_d1 and d2 >= max_d2:
                        break
                d11, d22 = 0, 0
                while True:
                    if d11 < max_d1:
                        d11 += 1
                    if d22 < max_d2:
                        d22 += 1
                    bound[x + d1 + d22][y - d1 + d22] = 1
                    bound[x + d2 + d11][y + d2 - d11] = 1
                    if d11 >= max_d1 and d22 >= max_d2:
                        break
                # 선거구 계산
                for i in range(5):
                    calculate(i + 1, area, visited, x, y, d1, d2)
                area = area[1:]
                temp = max(area) - min(area)
                if ans > temp:
                    ans = temp
print(ans)
