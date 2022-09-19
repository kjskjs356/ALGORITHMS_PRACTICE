# 1238_Contact 문제풀이
# 2022-09-13

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def bfs(n):
    global result
    q.append(n)
    while q:
        num = q.popleft()
        for x in call_list[num]:
            if visited[x] == 0:
                visited[x] = visited[num] + 1
                q.append(x)

for tc in range(1, 11):
    N, first = map(int, input().split())
    arr = list(map(int, input().split()))
    call_list = [[] for _ in range((max(arr) + 1))]
    visited = [0] * (max(arr) + 1)
    result, idx = 0, 0
    q = deque()
    for i in range(N // 2):
        call_list[arr[2 * i]].append(arr[2 * i + 1])
    visited[first] = 1
    bfs(first)
    for i in range(1, len(visited)):
        if idx <= visited[i]:
            idx = visited[i]
            result = i
    print('#{} {}' .format(tc, result))