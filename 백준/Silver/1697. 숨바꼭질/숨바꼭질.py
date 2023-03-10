# 1697 숨바꼭질
from collections import deque


def bfs(s, e):
    q = deque()
    q.append((s, 0))
    visited = []
    visited.append(s)
    while q:
        x, cnt = q.popleft()
        if x == e:
           return cnt
        for next in (1, -1, x):
            nx = x + next
            if 0 <= nx <= 100000 and nx not in visited:
                visited.append(nx)
                q.append((nx, cnt + 1))


N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)