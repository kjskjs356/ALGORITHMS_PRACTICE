# 상어 초등학교 풀이

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
area = [[0] * N for _ in range(N)]
info = []
info_like = dict()
ans = 0
for i in range(N**2):
    info.append(list(map(int, input().split())))
    info_like[info[i][0]] = info[i][1:]
for i in range(N**2):
    # N 은 최소 3, 처음엔 모두 빈칸 이므로 첫 학생은 무조건 (2,2) 위치에 배정
    num = info[i][0]
    like = info[i][1:]
    if i == 0:
        area[1][1] = num
    else:
        seat = []
        tmp = []
        # 1. 빈 칸 중 해당 학생이 좋아하는 번호가 현재 위치와 인접한 칸에 가장 많은 칸 탐색
        max_cnt = 0
        for j in range(N):
            for k in range(N):
                if area[j][k] == 0:
                    # 4방향으로 탐색
                    cnt = 0
                    for l in range(4):
                        ni = j + dx[l]
                        nj = k + dy[l]
                        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
                            if area[ni][nj] in like:
                                cnt += 1
                    if max_cnt <= cnt:
                        max_cnt = cnt
                        tmp.append((j, k, cnt))

        # 2. 1을 만족하는 칸 중 비어있는 인접칸이 가장 많은 칸 선정
        tmp2 = []
        max_cnt2 = 0
        for arr in tmp:
            if arr[2] == max_cnt:
                cnt2 = 0
                for i in range(4):
                    ni = arr[0] + dx[i]
                    nj = arr[1] + dy[i]
                    if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and area[ni][nj] == 0:
                        cnt2 += 1
                if max_cnt2 <= cnt2:
                    max_cnt2 = cnt2
                    tmp2.append((arr[0], arr[1], cnt2))
        tmp2.sort(key=lambda x:(x[0], x[1]))
        # 3. 2를 만족하는 칸 중 (1)행이 가장 빠른칸 그 다음(2) 열이 가장 빠른 칸
        for arr in tmp2:
            if arr[2] == max_cnt2:
                area[arr[0]][arr[1]] = num
                break
            else:
                continue

# 배치 끝난 후 만족도 조사
for i in range(N):
    for j in range(N):
        cnt3 = 0
        # 4 방향 탐색
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
                if area[ni][nj] in info_like.get(area[i][j]):
                    cnt3 += 1
        if cnt3 > 0:
            ans += 10**(cnt3 - 1)
print(ans)