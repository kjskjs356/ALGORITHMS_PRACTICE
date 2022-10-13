# 어항정리 풀이

from collections import deque


def stack_bowl2(height):
    idx1, idx2 = 1, -1
    while len(bowl[idx1 - 1]) < height:
        if len(bowl[idx1 - 1]) == 0:
            idx1 += 1
            continue
        while bowl[idx1 - 1]:
            bowl[idx2].append(bowl[idx1 - 1].pop())
        idx1 += 1
        idx2 -= 1
        if idx1 == N - 1:
            return

def array_row():
    tmp_q = deque()
    idx = 0
    while bowl[idx] == 0:
        idx += 1
    while idx < N:
        while len(bowl[idx]) > 0:
            tmp_q.append(bowl[idx].popleft())
        idx += 1
    for i in range(N):
        bowl[i].append(tmp_q.popleft())


def bfs():
    for x in range(N):
        for y in range(max_len):
            if new_bowl[x][y] > 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < max_len:
                        if new_bowl[nx][ny] == 0 or new_bowl[x][y] <= new_bowl[nx][ny]:
                            continue
                        else:
                            tmp = (new_bowl[x][y] - new_bowl[nx][ny]) // 5
                            if tmp > 0:
                                bowl[x][y] -= tmp
                                bowl[nx][ny] += tmp


def max_height():
    max_len = 0
    for i in range(N):
        if max_len < len(bowl[i]):
            max_len = len(bowl[i])
    return max_len


def array_bowl():
    while tmp:
        arr = tmp.popleft()
        num = 0
        while arr:
            while len(bowl[num]) == 0:
                num += 1
            bowl[num].insert(1, arr.popleft())
            num += 1


def stack_bowl():
    stack_tmp = deque()
    for i in range(N):
        stack_tmp2 = deque()
        if len(bowl[i]) == 0:
            continue
        elif len(bowl[i]) == 1:
            break
        else:
            while bowl[i]:
                stack_tmp2.appendleft(bowl[i].pop())
        stack_tmp.append(stack_tmp2)
    return stack_tmp


# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, K = map(int, input().split())
arr = list(map(int, input().split()))
bowl = list(deque() for _ in range(N))
for i in range(N):
    bowl[i].append(arr[i])
ans = 0
# K번 어항 정리
while True:
    # 어항 정리가 필요없으면 중단
    max_cnt = max(bowl)
    min_cnt = min(bowl)
    if max_cnt[0] - min_cnt[0] <= K:
        break
    # 물고기 수 가장 적은 어항 각각 + 1
    cnt = min_cnt[0]
    for i in range(N):
        if bowl[i][0] == cnt:
            bowl[i][0] += 1
    # 어항 쌓기
    # 단계 1. 맨 왼쪽것만 올리기
    bowl[1].append(bowl[0].pop())
    # 단계 2. 더 불가능할때까지 어항 쌓기 반복
    while True:
        # 쌓기 더 할지 확인코드
        max_len = 0
        remain = 0
        for i in range(N):
            if max_len < len(bowl[i]):
                max_len = len(bowl[i])
            elif len(bowl[i]) == 1:
                remain += 1
        if max_len > remain:
            break
        # 쌓기 시작
        tmp = stack_bowl()
        array_bowl()
        max_len = max_height()
        new_bowl = [[0] * max_len for _ in range(N)]
        for i in range(N):
            if bowl[i]:
                j = 0
                while j < len(bowl[i]):
                    new_bowl[i][j] = bowl[i][j]
                    j += 1
    # 단계 3. 어항 물고기 수 조절
    bfs()
    # 단계 4. 다시 일렬로 정렬
    array_row()
    # 단계 5. 공중부양 작업(2번)
    stack_bowl2(2)
    stack_bowl2(4)
    # 단계 6. 어항 물고기 수 한번더 조절
    max_len = max_height()
    new_bowl = [[0] * max_len for _ in range(N)]
    for i in range(N):
        if bowl[i]:
            j = 0
            while j < len(bowl[i]):
                new_bowl[i][j] = bowl[i][j]
                j += 1
    bfs()
    # 일렬로 정렬
    array_row()
    max_cnt = max(bowl)
    min_cnt = min(bowl)
    ans += 1
    if max_cnt[0] - min_cnt[0] <= K:
        break
print(ans)