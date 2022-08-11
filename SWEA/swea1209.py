# 1209 Sum 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    num = input()
    array=[]
    result = 0
    for _ in range(100):
        array.append(list(map(int, input().split())))
    sum_arr = []
    sum1, sum2, sum3 = 0, 0, 0
    #가로 합, 세로 합 동시에 확인
    for j in range(100):
        for k in range(100):
            sum1 += array[j][k]
            sum2 += array[k][j]
        sum_arr.append(sum1)
        sum_arr.append(sum2)
        sum1, sum2 = 0, 0
    #대각선 합
    for j in range(100):
        for k in range(100):
            if j == k:
                sum3 += array[j][k]
    sum3 = 0
    for x in sum_arr:
        if result < x:
            result = x
    print("#{} {}" .format(tc, result))