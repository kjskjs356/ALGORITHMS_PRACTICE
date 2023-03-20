# 14501 퇴사


def solve(day):
    if day > N: return -float('inf')
    if day == N: return 0
    if cache[day] != -1: return cache[day]
    cache[day] = max(solve(day + 1), solve(day + T[day]) + P[day])
    return cache[day]


N = int(input())
T = []
P = []
cache = [-1] * N
for _ in range(N):
    t, e = map(int, input().split())
    T.append(t)
    P.append(e)

ans = solve(0)
print(ans)