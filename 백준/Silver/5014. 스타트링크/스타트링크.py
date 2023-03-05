# 5014 스타트링크
from collections import deque


def bfs(s, g):
    q = deque()
    v = [0] * (F + 1)
    q.append(s)
    v[s] = 1
    while q:
        now = q.popleft()
        if now == g:
            return v[now] - 1
        for i in range(2):
            next = now + direct[i]
            if 1 <= next <= F and v[next] == 0:
                q.append(next)
                v[next] = v[now] + 1
    return 'use the stairs'


# 총 F층, 목표 G층, 강호 S층
# U버튼 : 위층 / D버튼 : 아래층
F, S, G, U, D = map(int, input().split())
direct = [U, -D]
ans = bfs(S, G)
print(ans)