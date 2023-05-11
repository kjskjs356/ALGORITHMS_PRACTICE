# 9095 1, 2, 3 더하기
from collections import deque


def bfs(n, target):
    global ans
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x > target:
            continue
        if x == target:
            ans += 1
            continue
        for dx in {1, 2, 3}:
            nx = x + dx
            q.append(nx)

T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    bfs(0, N)
    print(ans)
