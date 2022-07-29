# 2578 빙고

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
mc = []
for i in range(5):
    mc += list(map(int, input().split()))
num = 0

while True:
    breaker = False
    bingo_count = 0
    col_sum = 0
    count = 0


    for i in range(5): # 가로합 체크
        row_sum = 0
        for j in range(5):
            row_sum += bingo[i][j]
        if row_sum == 0:
            bingo_count += 1

    for i in range(5): # 세로합 체크
        row_sum = 0
        for j in range(5):
            row_sum += bingo[j][i]
        if row_sum == 0:
            bingo_count += 1
    
    #대각선 체크
    if (bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4]) == 0:
        bingo_count += 1
    if (bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0] ) == 0:
        bingo_count += 1
    
    if bingo_count >= 3:
        break

    for i in range(5):
        if breaker == True:
            break
        for j in range(5):
            if bingo[i][j] == mc[num]:
                bingo[i][j] = 0
                num += 1
                breaker = True
                break

print(num)