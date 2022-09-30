# 로봇청소기 풀이

# 북 동 남 서 / 왼쪽 방향 회전 시 + 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
# d => 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

# 멈출때까지 청소
while True:
    breaker = False
    # 1번 작업, 현재 위치 청소
    if not visited[r][c]:
        visited[r][c] = True
        ans += 1
    # 2번 작업, 4 방향 청소 여부 확인
    cnt = 0
    while cnt < 4:
        # 현재 위치 기준 왼쪽방향 여부 체크 후 전진
        nr = r + dr[(d + 3) % 4]
        nc = c + dc[(d + 3) % 4]
        if 0 <= nr < N and 0 <= nc < M:
            # 청소 가능한 경우
            if not visited[nr][nc] and area[nr][nc] != 1:
                # 1번 작업으로 복귀
                r, c = nr, nc
                d += 3
                breaker = True
                break
            # 청소 공간 없음(이미 청소 or 벽)
            else:
                # 2번 작업으로 복귀
                d += 3
                cnt += 1
        # 청소 공간 없음(격자 벗어남)
        else:
            # 2번 작업으로 복귀
            d += 3
            cnt += 1
    if breaker:
        continue
    # 4 방향 모두 청소 되어있음 or 벽
    # 후진 가능하면 2번 복귀, 불가능하면 작동 중지
    nr = r - dr[d % 4]
    nc = c - dc[d % 4]
    if 0 <= nr < N and 0 <= nc < M:
        # 뒤에 공간있으면 후진 뒤 2번 작업으로 복귀
        if area[nr][nc] != 1:
            r, c = nr, nc
            continue
        # 후진 시 벽이 있을 경우 작동 중지
        else:
            break
    # 후진 시 격자 벗어난 겨우 작동 중지
    else:
        break
print(ans)
