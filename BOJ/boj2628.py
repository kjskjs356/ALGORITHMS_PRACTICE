# 2628 종이자르기

# 가로,세로
W, H = map(int, input().split())
N = int(input())
# 0: 가로, 1: 세로
cut = []
for _ in range(N):
    cut.append(list(map(int, input().split())))
#종이의 양끝 요소 삽입
cut.append([0, 0])
cut.append([0, H])
cut.append([1, 0])
cut.append([1, W])
cut.sort(key=lambda x:(x[0], x[1]))
max_w, max_h = 0, 0
for i in range(1, N + 4):
    if cut[i][0] == 0:
        if max_h < cut[i][1] - cut[i - 1][1]:
            max_h = cut[i][1] - cut[i - 1][1]
    elif cut[i][0] == 1:
        if cut[i - 1][0] == 0:
            continue
        else:
            if max_w < cut[i][1] - cut[i - 1][1]:
                max_w = cut[i][1] - cut[i - 1][1]
print(max_h * max_w)