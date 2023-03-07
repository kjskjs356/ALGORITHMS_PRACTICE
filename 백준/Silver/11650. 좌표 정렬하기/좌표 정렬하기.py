# 11650 좌표 정렬하기

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[0], x[1]))
for x in arr:
    print(x[0], x[1])