# 2475 검증

arr = list(map(int, input().split()))
ans = 0
for x in arr:
    ans += x**2
ans %= 10
print(ans)