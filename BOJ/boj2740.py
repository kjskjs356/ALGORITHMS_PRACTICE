# 2740_행렬 곱셈

N, M = map(int, input().split())
A, B = [], []
for i in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))
result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        tmp = 0
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        result[i][j] = tmp
for i in range(N):
    print(*result[i])