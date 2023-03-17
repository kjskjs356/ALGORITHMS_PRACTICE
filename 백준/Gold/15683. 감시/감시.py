# 15683 감시


# 중복순열
def product(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for j in product(arr, n - 1):
                yield [arr[i]] + j


N, M = map(int, input().split())
area = []
cctv = []
ans = float('inf')
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if 0 < arr[j] < 6:
            cctv.append((i, j, arr[j]))
    area.append(arr)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if len(cctv) == 0:
    temp = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                temp += 1
    print(temp)
else:
    # 방향을 남 북 동 서 0, 1, 2, 3으로 설정
    for arr in product([0, 1, 2, 3], len(cctv)):
        area2 = [arr[:] for arr in area]
        # cctv 순서대로 감시지역 체크
        for i in range(len(cctv)):
            x, y, type = cctv[i][0], cctv[i][1], cctv[i][2]
            if type == 1:
                num = 1
                while True:
                    nx = x + dx[arr[i]] * num
                    ny = y + dy[arr[i]] * num
                    # 범위 안쪽 & 벽 없는지 체크
                    if 0 <= nx < N and 0 <= ny < M and area2[nx][ny] != 6:
                        # cctv 있는 자리면 다음칸으로 이동
                        if area2[nx][ny] > 0:
                            num += 1
                        else:
                            # 감시한 자리는 9로 표시
                            area2[nx][ny] = 9
                            num += 1
                    else:
                        break
            elif type == 2:
                num, num2 = 1, 1
                flag1, flag2 = True,  True
                while flag1 or flag2:
                    if flag1:
                        nx = x + dx[arr[i]] * num
                        ny = y + dy[arr[i]] * num
                        if 0 <= nx < N and 0 <= ny < M and area2[nx][ny] != 6:
                            # cctv 있는 자리면 다음칸으로 이동
                            if area2[nx][ny] > 0:
                                num += 1
                            else:
                                # 감시한 자리는 9로 표시
                                area2[nx][ny] = 9
                                num += 1
                        else:
                            flag1 = False
                    if flag2:
                        nx2 = x + dx[(arr[i] + 2) % 4] * num2
                        ny2 = y + dy[(arr[i] + 2) % 4] * num2
                        #한쪽부터 체크
                        if 0 <= nx2 < N and 0 <= ny2 < M and area2[nx2][ny2] != 6:
                            # cctv 있는 자리면 다음칸으로 이동
                            if area2[nx2][ny2] > 0:
                                num2 += 1
                            else:
                                # 감시한 자리는 9로 표시
                                area2[nx2][ny2] = 9
                                num2 += 1
                        else:
                            flag2 = False
            elif type == 3:
                # 현방향 + 90도 회전방향 검사
                for j in range(2):
                    num = 1
                    while True:
                        nx = x + dx[(arr[i] + j) % 4] * num
                        ny = y + dy[(arr[i] + j) % 4] * num
                        if 0 <= nx < N and 0 <= ny < M and area2[nx][ny] != 6:
                            # cctv 있는 자리면 다음칸으로 이동
                            if area2[nx][ny] > 0:
                                num += 1
                            else:
                                # 감시한 자리는 9로 표시
                                area2[nx][ny] = 9
                                num += 1
                        else:
                            break
            elif type == 4:
                # 한 방향만 빼고 모두 검사
                for j in range(3):
                    num = 1
                    while True:
                        nx = x + dx[(arr[i] + j) % 4] * num
                        ny = y + dy[(arr[i] + j) % 4] * num
                        if 0 <= nx < N and 0 <= ny < M and area2[nx][ny] != 6:
                            # cctv 있는 자리면 다음칸으로 이동
                            if area2[nx][ny] > 0:
                                num += 1
                            else:
                                # 감시한 자리는 9로 표시
                                area2[nx][ny] = 9
                                num += 1
                        else:
                            break
            elif type == 5:
                # 4방향을 감시하므로 방향 경우의수를 1가지만 체크해도 상관없다
                if arr[i] == 0:
                    # 모든 방향 검사
                    for j in range(4):
                        num = 1
                        while True:
                            nx = x + dx[(arr[i] + j) % 4] * num
                            ny = y + dy[(arr[i] + j) % 4] * num
                            if 0 <= nx < N and 0 <= ny < M and area2[nx][ny] != 6:
                                # cctv 있는 자리면 다음칸으로 이동
                                if area2[nx][ny] > 0:
                                    num += 1
                                else:
                                    # 감시한 자리는 9로 표시
                                    area2[nx][ny] = 9
                                    num += 1
                            else:
                                break

        # 사각지대 체크
        temp = 0
        breaker = False
        for i in range(N):
            if breaker:
                break
            for j in range(M):
                if area2[i][j] == 0:
                    temp += 1
                    if temp >= ans:
                        breaker = True
                        break
        if breaker:
            continue
        ans = min(ans, temp)
    print(ans)