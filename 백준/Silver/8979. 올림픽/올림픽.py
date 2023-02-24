# 8979 올림픽

N, K = map(int, input().split())
score = []
for i in range(N):
    score.append(list(map(int, input().split())))
rank = [0 for _ in range(N)]
cnt = 1
num = 1
score.sort(key = lambda x : [x[1], x[2], x[3]], reverse=True)
for i in range(1, N + 1):
    if i == 1:
        rank[score[i - 1][0] - 1] = cnt
    else:
        if score[i - 2][1:4] == score[i - 1][1: 4]:
            rank[score[i - 1][0] - 1] = cnt
            num += 1
        else:
            rank[score[i - 1][0] - 1] = cnt + num
            cnt += num
            num = 0
print(rank[K - 1])