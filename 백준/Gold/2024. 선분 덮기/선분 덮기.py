# 2024 선분덮기

# 0부터 M 까지의 범위를 선으로 덮기
M = int(input())
line = []
total = [0] * (M + 1)
ans = 0
# 선 정보 입력(0, 0) 나오면 종료
while True:
    L, R = map(int, input().split())
    if L > R: L, R = R, L
    if L == 0 and R == 0: break
    if L == R or L > M or R < 0: continue
    line.append((L, R))
line.sort(key=lambda x:(x[0], x[1]))
cur = 0
idx = 0
while True:
    end = -1
    # 선분의 시작점이 전체 시작점 이하일 경우
    while idx < len(line):
        if line[idx][0] <= cur:
            if line[idx][1] > end:
                end = line[idx][1]
            idx += 1
        else:
            break
    if end == -1:
        print(0)
        break
    ans += 1
    if end >= M:
        print(ans)
        break
    cur = end