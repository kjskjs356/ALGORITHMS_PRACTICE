# 10163 색종이

N = int(input())
board = [[0] * 1001 for _ in range(1001)]
color = [0] * N
for i in range(1, N + 1):
    paper = list(map(int, input().split()))
    for j in range(paper[0], paper[0] + paper[2]):
        for k in range(paper[1], paper[1] + paper[3]):
            board[j][k] = i
for i in range(1, N + 1):
    for j in range(1001):
        for k in range(1001):
            if board[j][k] == i:
                color[i - 1] += 1
for i in range(N):
    print(color[i])