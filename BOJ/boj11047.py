# 11047 동전 0 풀이

N, K = map(int, input().split())
arr = []
result = 0
for _ in range(N):
    arr.append(int(input()))

for i in range(len(arr)-1, -1, -1):
    result += K // arr[i]
    K %= arr[i]

print(result)