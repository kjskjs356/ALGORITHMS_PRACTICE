# 18111 마인크래프트

N, M, B = map(int, input().split())
arr = []
ans = []
for i in range(N):
    arr += (map(int, input().split()))

for i in range(min(arr), max(arr) + 1):
    bag = B
    sec = 0
    for ground in arr:
        if (ground - i) > 0:
            bag += (ground - i)
            sec += 2 * (ground - i)
        elif (ground - i) < 0:
            bag += (ground - i)
            sec += 1 * (ground - i) * -1
    if bag >= 0:
        ans.append([sec, i])

ans.sort(key=lambda x: (x[0], -x[1]))
print(ans[0][0], ans[0][1])