# 1974 스도쿠검증 풀이

def square(arr, width, height):
    result = 0
    for i in range(width, width + 3):
        for j in range(height, height + 3):
            result += arr[i][j]
    if result == 45:
        return 1
    else:
        return 0

T = int(input())

for t in range(1, T + 1):
    number_list = list()
    true_false = True
    
#입력과 동시에 가로줄 먼저 확인
    for i in range(9):
        number_list.append(list(map(int, input().split())))
        if sum(number_list[i]) == 45:
            continue
        else:
            true_false = False

# 세로 합계 구한 후, 45(1~9까지의 총합계) 확인
    for i in range(9):
        Sum = 0
        for j in range(9):
            Sum += number_list[j][i]
        if Sum == 45:
            continue
        else:
            true_false = False

#블록 별로 합 45 체크
    for i in range(3):
        for j in range(3):
            if square(number_list, 3 * i, 3 * j):
                continue
            else:
                true_false = False


    if true_false:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
