# 1039 교환

from collections import deque


def bfs(n, k):
    global ans
    visited = set()
    q = deque()
    q.append((n, 0))
    while q:
        now, cnt = q.pop()
        if cnt == k:
            ans = max(ans, now)
            continue
        arr = list(map(int, str(now)))
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                # 맨 앞자리 수는 0이 될수 없음
                if i == 0 and arr[j] == 0: continue
                arr[i], arr[j] = arr[j], arr[i]
                num = int(''.join(list(map(str, arr))))
                if (num, cnt + 1) not in visited:
                    q.appendleft((num, cnt + 1))
                    visited.add((num, cnt + 1))
                arr[i], arr[j] = arr[j], arr[i]


N, K = map(int, input().split())
ans = 0
bfs(N, K)
if ans == 0:
    print(-1)
else:
    print(ans)