# 10158 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
x, y = h - q, p
#45방향기준 반시계방향
dx = [-1, 1]
dy = [1, -1]

t = int(input())
n = 0
i = 0
j = 0
while n <= t:
    if n == t:
        break
    nx, ny = x + dx[i % 2], y + dy[j % 2]
    if not (0 <= nx <= h) and not (0 <= ny <= w):
        i += 1
        j += 1
        n += 1
        x = x + dx[i % 2]
        y = y + dy[j % 2]
    elif not (0 <= nx <= h):
        i += 1
        n += 1
        x = x + dx[i % 2]
        y = y + dy[j % 2]
    elif not (0 <= ny <= w):
        j += 1
        n += 1
        x = x + dx[i % 2]
        y = y + dy[j % 2]
    else:
        n += 1
        x, y = nx, ny
print(y, h - x)