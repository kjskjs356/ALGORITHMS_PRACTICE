# 1244_ 최대상금 풀이
# 2022-09-21


def dfs(idx, now):
    global result
    if now == cnt:
        result = max(result, sum_arr(num))
        return
    for i in range(idx, len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            dfs(i, now + 1)
            num[i], num[j] = num[j], num[i]


def sum_arr(arr):
    result = 0
    j = 0
    for i in range(len(arr)-1, -1, -1):
        result += arr[i] * 10**j
        j += 1
    return result


T = int(int(input()))
for tc in range(1, T + 1):
    num, cnt = input().split()
    cnt = int(cnt)
    num = list(map(int, list(num)))
    if cnt > len(num):
        cnt = len(num)
    result = 0
    dfs(0, 0)
    print('#{} {}' .format(tc, result))
