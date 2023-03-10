# 16236 아기 상어
from collections import deque

def bfs(a, b, size, size_up):
    q = deque()
    cnt = 0
    q.append((a, b, cnt, size, size_up))
    eatting = False
    v = [[False for _ in range(N)] for _ in range(N)]
    v[a][b] = True
    stack = []
    while q:
        x, y, cnt, size, size_up = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
                # 상어보다 작은 물고기면 잡아먹고 탐색 마무리
                if size > board[nx][ny] and board[nx][ny] > 0:
                    v[nx][ny] = True
                    stack.append((nx, ny, cnt + 1))
                # 크기 같거나 빈공간이면 그냥 지나가기
                elif size == board[nx][ny] or board[nx][ny] == 0:
                    v[nx][ny] = True
                    q.append((nx, ny, cnt + 1, size, size_up))
    if len(stack) == 0:
        return a, b, False, 0, size, size_up
    stack.sort(key=lambda x : (x[2], x[0], x[1]))
    board[stack[0][0]][stack[0][1]] = 0
    size_up += 1
    if size == size_up:
        size += 1
        size_up = 0
    return stack[0][0], stack[0][1], True, stack[0][2],  size, size_up

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
# 아기 상어 초기 사이즈
size = 2
size_up = 0
ans = 0

board = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 9:
            # 상어 최초 좌표
            x, y = i, j
            arr[j] = 0
    board.append(arr)

# 상어가 먹을 수 있는 물고기가 더이상 없을때까지 반복
while True:
    temp = 0
    is_eat = False
    # 상어가 탐색하는 동안 물고기를 먹었으면 계속, 한마리도 못먹으면 어미상어 호출(종료)
    x, y, is_eat, temp, size, size_up = bfs(x, y, size, size_up)
    if not is_eat:
        break
    ans += temp
print(ans)