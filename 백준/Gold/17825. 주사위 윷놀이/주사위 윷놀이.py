# 17825 주사위 윷놀이

def product(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for j in product(arr, n - 1): # arr[i:] 대신 arr 통째로 사용
                yield [arr[i]] + j

# 윳놀이 경로 설정
route = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [0, 13, 16, 19, 25, 30, 35, 40],
    [0, 22, 24, 25, 30, 35, 40],
    [0, 28, 27, 26, 25, 30, 35, 40]]

dice = list(map(int, input().split()))
ans = 0

for arr in product([0, 1, 2, 3], 10):
    # 말의 현재 칸의 인덱스
    horse = [0, 0, 0, 0]
    # 말이 현재 밟고 있는 칸의 [칸 값, 루트 값, 빨간루트 여부]
    horse_now = [[-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [-1, 0, 0]]
    # 말의 경로 여부
    # 말의 칸 누적합
    horse_sum = [0, 0, 0, 0]
    reach = [False, False, False, False]
    temp = 0
    flag = True
    for i in range(10):
        # arr : 선택된 말의 번호(0 ~ 3), horse : 말의 현재 위치,  horse_route : 현재 말의 경로(0, 1, 2, 3)
        if horse_now[arr[i]][0] in (10, 20, 30) and horse_now[arr[i]][1] == 0:
            horse_now[arr[i]][1] = route[horse_now[arr[i]][1]][horse[arr[i]]] // 10
            horse[arr[i]] = 0
            horse_now[arr[i]][2] = 1
        # 이미 도착한 말이면 패스
        if reach[arr[i]]:
            flag = False
            break
        next_step = horse[arr[i]] + dice[i]
        # 말이 종착점인지 아닌지 체크
        if next_step >= len(route[horse_now[arr[i]][1]]):
            reach[arr[i]] = True
            horse[arr[i]] = 0
            horse_now[arr[i]] = [-1, 0, 0]
            continue
        # 이동하려는 칸에 다른 말이 있으면 스탑
        if route[horse_now[arr[i]][1]][next_step] in (16, 22, 24, 26, 28, 30):
            for j in range(4):
                if arr[i] == j:
                    continue
                if [route[horse_now[arr[i]][1]][next_step], horse_now[arr[i]][2]] == [horse_now[j][0], horse_now[j][2]]:
                    flag = False
                    break
        else:
            if route[horse_now[arr[i]][1]][next_step] in (horse_now[0][0], horse_now[1][0], horse_now[2][0], horse_now[3][0]):
                flag = False
                break
        horse_now[arr[i]][0] = route[horse_now[arr[i]][1]][next_step]
        horse_sum[arr[i]] += route[horse_now[arr[i]][1]][next_step]
        horse[arr[i]] = next_step
    if not flag:
        continue
    if ans < sum(horse_sum):
        ans = sum(horse_sum)
print(ans)
