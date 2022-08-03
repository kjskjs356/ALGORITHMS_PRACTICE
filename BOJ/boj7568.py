# 7568 덩치

N = int(input())
physical = []
rank_list = []
for i in range(N):
    physical.append(list(map(int, input().split())))

# 순서대로 비교
for i in range(N):
    rank = 1
    for j in range(N):
        if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]: # 키, 몸무게 조건 둘 다 만족하면 등수 체크
            rank += 1
        else:
            continue
    rank_list.append(rank)

for i in range(N):
    if i == N-1:
        print(rank_list[i], end='')
    else:
        print(rank_list[i], end=' ')