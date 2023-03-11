# 1920 수 찾기

N = int(input())
num = dict()
arr = list(map(int, input().split()))
for x in arr:
    if not num.get(x):
        num[x] = x
    else:
        continue
M = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    if num.get(x):
        print(1)
    else:
        print(0)