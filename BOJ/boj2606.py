# 2606 바이러스

# x: 시작 노드
def dfs(x):
    global result
    if not visited[x]:
        visited[x] = True
        result += 1
        for w in node[x]:
            if not visited[w]:
                stack.append(w)
                dfs(w)
        if stack == []:
            # 1번은 제외해야 하므로 -1
            result -= 1
            return
        stack.pop()

N = int(input())
K = int(input())

# 노드 간선 정보
node = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(K):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
stack = []
result = 0
dfs(1)
print(result)