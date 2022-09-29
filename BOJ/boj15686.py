# 치킨 배달 풀이


def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


def bfs(arr):
    # 각 집마다 체크
    total_distacne = 0
    for x, y in home:
        distance = float('inf')
        # 가장 가까운 치킨집으로 거리 갱신
        for a, b in arr:
            tmp = abs(x - a) + abs(y - b)
            if tmp < distance:
                distance = tmp
        total_distacne += distance
    return total_distacne

N, M = map(int, input().split())
area = []
chicken = []
c_list = []
home = []
ans = float('inf')
for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        if area[i][j] == 2:
            chicken.append((i, j))
        elif area[i][j] == 1:
            home.append((i, j))
visited = [False] * len(chicken)
arr = comb(chicken, M)
for x in arr:
    distance = bfs(x)
    if ans > distance:
        ans = distance
print(ans)