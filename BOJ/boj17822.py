# 17822 원판 돌리기

from collections import deque

# N : 반지름
# M : 원판에 있는 숫자갯수
# T : 회전 수
N, M, T = map(int, input().split())
circle = deque([list(map(int, input().split())) for _ in range(N)])
x, d, k = [], [], []
for _ in range(T):
    # x : 배수, d : 방향, k : 회전 칸 수
    a, b, c = map(int, input().split())
    x.append(a)
    d.append(b)
    k.append(c)

for i in range(T):
    for j in range(1, N + 1):
        # 배수 체크
        if (j + 1) % x[i] == 0:
            # 0이면 시계방향, 1이면 반시계방향
            if d[i] == 0:
                circle[j].rotate(k[i])
            elif d[i] == 1:
                circle[j].rotate(-k[i])
