# 2382_미생물 격리 풀이
# 2022-09-23

from collections import deque

# X 상 하 좌 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    # N: 약품 면적, M: 시간, K: 미생물 군집 정보
    N, M, K = map(int, input().split())
    field = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        r, c, m, d = map(int, input().split())
        field[r][c].append([m, d])

    for _ in range(M):
        # 미생물 이동
        new_field = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if field[i][j] != []:
                    for k in range(len(field[i][j])):
                        ni, nj = i, j
                        m, d = field[i][j].pop(0)
                        ni = ni + dx[d]
                        nj = nj + dy[d]
                        new_field[ni][nj].append([m, d])
        # 기존 필드로 복제
        for i in range(N):
            for j in range(N):
                if new_field[i][j]:
                    for arr in new_field[i][j]:
                        field[i][j].append(arr)
        #중복된 칸은 합성, 테두리에 있는 집군은 절반 소멸
        for i in range(N):
            for j in range(N):
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    if field[i][j]:
                        field[i][j][0][0] //= 2
                        #방향 바꾸기
                        if field[i][j][0][1] == 1:
                            field[i][j][0][1] = 2
                        elif field[i][j][0][1] == 2:
                            field[i][j][0][1] = 1
                        elif field[i][j][0][1] == 3:
                            field[i][j][0][1] = 4
                        elif field[i][j][0][1] == 4:
                            field[i][j][0][1] = 3
                else:
                    if len(field[i][j]) >= 2:
                        sum_m = 0
                        for micro in field[i][j]:
                            sum_m += micro[0]
                        # 제일 큰 집군을 기준으로 방향 확정
                        max_m, d = 0, 0
                        for arr in field[i][j]:
                            if max_m < arr[0]:
                                max_m = arr[0]
                                d = arr[1]
                        # 합쳐지고 난뒤 배열 속 요소 우선 제거
                        for _ in range(len(field[i][j])):
                            field[i][j].pop()
                        # 합친 값 토대로 새로운 미생물집군 추가
                        field[i][j].append([sum_m, d])
    # 미생물 총합 계산
    result = 0
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                for arr in field[i][j]:
                    result += arr[0]
    print('#{} {}' .format(tc, result))
