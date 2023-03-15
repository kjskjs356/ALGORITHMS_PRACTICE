# 9019 DSLR
from collections import deque


def bfs(num, ans):
    q = deque()
    q.append((num, []))
    visited = [0] * 10000
    while q:
        x, arr = q.popleft()
        visited[int(x)] = 1
        if x == ans:
            return arr
        for com in ('D', 'S', 'L', 'R'):
            temp_arr = arr[:]
            if com == 'D':
                word = int(x) * 2
                if word > 9999:
                    word %= 10000
                if not visited[word]:
                    visited[word] = 1
                    temp_arr.append('D')
                    q.append((word, temp_arr))
            elif com == 'S':
                word = int(x) - 1
                if word < 0:
                    word = 9999
                if not visited[word]:
                    visited[word] = 1
                    temp_arr.append('S')
                    q.append((word, temp_arr))
            elif com == 'L':
                temp = 0
                temp += x * 10
                temp += x // 1000
                if temp // 10 == 0:
                    temp *= 10
                else:
                    temp %= 10000
                if not visited[temp]:
                    visited[temp] = 1
                    temp_arr.append('L')
                    q.append((temp, temp_arr))
            elif com == 'R':
                temp = 0
                temp += x // 10
                temp += 1000 * (x % 10)
                if not visited[temp]:
                    visited[temp] = 1
                    temp_arr.append('R')
                    q.append((temp, temp_arr))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    command = bfs(A, B)
    print(''.join(command))