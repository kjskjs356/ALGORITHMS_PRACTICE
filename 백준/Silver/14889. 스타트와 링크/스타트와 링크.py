# 14889 스타트와 링크


def back(idx, cnt):
    global ans, N
    sum1, sum2 = 0, 0
    if cnt == N // 2:
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if visited[i] and visited[j]:
                    sum1 += area[i][j]
                elif not visited[i] and not visited[j]:
                    sum2 += area[i][j]
        temp = abs(sum1 - sum2)
        ans = min(ans, temp)
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            back(i, cnt + 1)
            visited[i] = False


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
ans = float('inf')
back(0, 0)
print(ans)