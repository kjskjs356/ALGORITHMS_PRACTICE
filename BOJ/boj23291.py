# 어항정리 풀이

from collections import deque


def array_bowl(idx):
    while tmp:
        arr = tmp.pop()
        num = len(arr)
        


def stack_bowl():
    tmp = deque()
    tmp2 = []
    for i in range(N):
        if len(bowl[i]) == 0:
            continue
        elif len(bowl[i]) == 1:
            break
        else:
            while bowl[i]:
                tmp2.append(bowl[i].pop())
            tmp.append(tmp2)
    return tmp


N, K = map(int, input().split())
arr = list(map(int, input().split()))
bowl = list(deque() for _ in range(N))
for i in range(N):
    bowl[i].append(arr[i])
# K번 어항 정리
for _ in range(1):
    # 물고기 수 가장 적은 어항 각각 + 1
    cnt = min(arr)
    for i in range(N):
        if bowl[i][0] == cnt:
            bowl[i][0] += 1
    # 어항 쌓기
    # 단계 1. 맨 왼쪽것만 올리기
    bowl[1].append(bowl[0].pop())
    print(bowl)
    # 단계 2. 더 불가능할때까지 어항 쌓기 반복
    while True:
        max_len = 0
        remain = 0
        for i in range(N):
            if max_len < len(bowl[i]):
                max_len = len(bowl[i])
            elif len(bowl[i]) == 1:
                remain += 1
        if max_len > remain:
            break
        tmp = stack_bowl()
        for i in range(N):
            if bowl[i]:
                idx = i
        array_bowl(idx)
        break
