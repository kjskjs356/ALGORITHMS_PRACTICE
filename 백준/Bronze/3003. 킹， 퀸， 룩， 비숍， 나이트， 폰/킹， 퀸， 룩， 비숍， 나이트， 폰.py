# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

# 본래 배열상태
origin = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
ans = []
for i in range(len(arr)):
    ans.append(origin[i] - arr[i])
print(*ans)