# 2231 분해합

N = int(input())
ans = N
for num in range(1, N):
    now = num
    temp = 0
    temp += now
    while now:
        temp += now % 10
        now //= 10
    if temp == N:
        ans = min(ans, num)
if ans == N:
    print(0)
else:
    print(ans)