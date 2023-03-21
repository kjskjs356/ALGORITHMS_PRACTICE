# 2048(Easy)


def move(arr, n):
    # 상 이동
    if n == 0:
        for i in range(N):
            for j in range(N):
                # 0이 아닌 칸 발견
                if arr[j][i] != 0:
                    for k in range(j + 1, N):
                        if arr[k][i] == arr[j][i]:
                            arr[j][i] *= 2
                            arr[k][i] = 0
                            break
                        elif arr[k][i] == 0:
                            continue
                        else:
                            break
        # 합산 끝난 후 각 열 밀착시키기
        for i in range(N):
            for j in range(N):
                # 위에서부터 빈칸 체크
                if arr[j][i] == 0:
                    for k in range(j + 1, N):
                        # 빈칸을 시작으로 빈칸아닌 곳까지 아래로 내려가다가 빈칸이 아닌 칸과 교체
                        if arr[k][i] != 0:
                            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
                            break
    # 하 이동
    elif n == 1:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                # 0이 아닌 칸 발견
                if arr[j][i] != 0:
                    for k in range(j - 1, -1, -1):
                        if arr[k][i] == arr[j][i]:
                            arr[j][i] *= 2
                            arr[k][i] = 0
                            break
                        elif arr[k][i] == 0:
                            continue
                        else:
                            break
        # 합산 끝난 후 각 열 밀착시키기
        for i in range(N):
            for j in range(N - 1, -1, -1):
                # 밑에서부터 빈칸 체크
                if arr[j][i] == 0:
                    for k in range(j - 1, -1, -1):
                        # 빈칸을 시작으로 빈칸아닌 곳까지 위로 올라가다가 빈칸이 아닌 칸과 교체
                        if arr[k][i] != 0:
                            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
                            break
    # 좌 이동
    elif n == 2:
        for i in range(N):
            for j in range(N):
                # 0이 아닌 칸 발견
                if arr[i][j] != 0:
                    for k in range(j + 1, N):
                        if arr[i][k] == arr[i][j]:
                            arr[i][j] *= 2
                            arr[i][k] = 0
                            break
                        elif arr[i][k] == 0:
                            continue
                        else:
                            break
        # 합산 끝난 후 각 열 밀착시키기
        for i in range(N):
            for j in range(N):
                # 왼쪽에서부터 빈칸 체크
                if arr[i][j] == 0:
                    for k in range(j + 1, N):
                        # 빈칸을 시작으로 빈칸아닌 곳까지 왼쪽으로 이동하다가 빈칸이 아닌 칸과 교체
                        if arr[i][k] != 0:
                            arr[i][j], arr[i][k] = arr[i][k], arr[i][j]
                            break
    # 우 이동
    elif n == 3:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                # 0이 아닌 칸 발견
                if arr[i][j] != 0:
                    for k in range(j - 1, -1, -1):
                        if arr[i][k] == arr[i][j]:
                            arr[i][j] *= 2
                            arr[i][k] = 0
                            break
                        elif arr[i][k] == 0:
                            continue
                        else:
                            break
        # 합산 끝난 후 각 열 밀착시키기
        for i in range(N):
            for j in range(N - 1, -1, -1):
                # 오른쪽에서부터 빈칸 체크
                if arr[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        # 빈칸을 시작으로 빈칸아닌 곳까지 왼쪽으로 이동하다가 빈칸이 아닌 칸과 교체
                        if arr[i][k] != 0:
                            arr[i][j], arr[i][k] = arr[i][k], arr[i][j]
                            break


def back(arr, cnt):
    global ans
    if cnt == 5:
        temp = max(map(max, arr))
        ans = max(ans, temp)
        return
    for i in range(4):
        area2 = [clone_arr[:] for clone_arr in arr]
        move(area2, i)
        back(area2, cnt + 1)



N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
ans = 2
if N == 1:
    print(area[0][0])
else:
    back(area, 0)
    print(ans)