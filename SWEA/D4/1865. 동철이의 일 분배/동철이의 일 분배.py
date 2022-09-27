# 1865_동철이의 일분배 풀이
# 2022-09-27


def back(idx, tmp):
    global ans
    if sum(visited) == N:
        if ans < tmp:
            ans = tmp
            return
    if ans >= tmp:
        return
    for i in range(N):
        if not visited[i]:
            if not P[idx][i] == 0:
                tmp2 = tmp * P[idx][i] * 0.01
                visited[i] = True
                back(idx + 1, tmp2)
                visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    tmp = 1
    visited = [0] * N
    back(0, tmp)
    print('#{} {}' .format(tc, format(ans * 100,".6f")))