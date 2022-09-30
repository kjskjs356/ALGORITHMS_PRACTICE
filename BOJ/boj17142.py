# 연구소3 풀이

from collections import deque


def bfs(arr):
    q = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        q[i] = deque()
        q[i].append((arr[i][0], arr[i][1], 0))
        new_area[arr[i][0]][arr[i][1]] = 2
    while True:
        is_zero = True
        for i in range(N):
            print(new_area[i])
        print()
        q_check = False
        for i in range(len(arr)):
            for j in range(N):
                for k in range(N):
                    if area[j][k] == 0:
                        is_zero = False
            if not q[i]:
                continue
            num = len(q[i])
            for _ in range(num):
                x, y, cnt = q[i].popleft()
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < N and 0 <= ny < N:
                        if new_area[nx][ny] == 0 or new_area[nx][ny] == -2:
                            new_area[nx][ny] = cnt + 1
                            q[i].append((nx, ny, cnt + 1))
        if is_zero:
            break
        # q가 하나라도 요소가 남아있다면 계속 반복
        for i in range(len(arr)):
            if q[i]:
                q_check = True
        # q가 모두 비었으면 중단
        if not q_check:
            break

def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[1 + i:], n - 1):
                result.append([arr[i]] + j)
    return result

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


N, M = map(int, input().split())
area = []
virus_arr = []
for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        if area[i][j] == 2:
            virus_arr.append((i, j))
# 빈공간이 없으면 0 출력
is_none_zero = True
for i in range(N):
    for j in range(N):
        if area[i][j] == 0:
            is_none_zero = False
if is_none_zero:
    ans = 0
else:
    virus = comb(virus_arr, M)
    ans = float('inf')

    for v in virus:
        check = False
        breaker = False
        new_area = [arr[:] for arr in area]
        for i in range(N):
            for j in range(N):
                if new_area[i][j] == 2:
                    new_area[i][j] = -2
                if new_area[i][j] == 1:
                    new_area[i][j] = -1
        bfs(v)
        # 모든 빈칸에 바이러스를 퍼뜨린 경우에만 최소값갱신
        for i in range(N):
            if breaker:
                break
            for j in range(N):
                if i == j:
                    continue
                else:
                    if new_area[i][j] == 0:
                        check = True
                        breaker = True
                        break
        if check:
            continue
        max_val = max(map(max, new_area))
        if ans > max_val:
            ans = max_val

if ans == float('inf'):
    ans = -1
print(ans)
