# 2116 주사위 쌓기

# 인덱스 0:5 , 1:3, 2:4 페어
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
max_result = []

for i in range(6):
    start = i # 윗면 인덱스
    result = 0 # 윗면 경우의수 마다 합 저장

    for j in range(N):
        if start == 0 or start == 5: # 윗면이 0 또는 5
            result += max(dice[j][1:5]) # 옆면중 최고 값 합
            if j < N  - 1 and start == 0:
                start = dice[j + 1].index(dice[j][5])
            elif j < N - 1 and start == 5:
                start = dice[j + 1].index(dice[j][0])

        elif start == 1 or start == 3: # 윗면이 1 또는 3
            result += max([dice[j][0]] + [dice[j][2]] + dice[j][4:])
            if j < N - 1 and start == 1:
                start = dice[j + 1].index(dice[j][3])

            elif j < N - 1 and start == 3:
                start = dice[j + 1].index(dice[j][1])


        elif start == 2 or start == 4: # 윗면이 2 또는 4
            result += max(dice[j][0:2] + [dice[j][3]] + [dice[j][5]])
            if j < N - 1 and start == 2:
                start = dice[j + 1].index(dice[j][4])

            elif j < N - 1 and start == 4:
                start = dice[j + 1].index(dice[j][2])

    max_result.append(result)

print(max(max_result))
