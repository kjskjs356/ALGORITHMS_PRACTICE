# 4836 색칠하기 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    color_map = [[0] * 10 for _ in range(10)]
    arr = []
    N = int(input())
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    result = 0
    #순서대로 색칠
    for i in range(N):
        for j in range(arr[i][0], arr[i][2] + 1):
            for k in range(arr[i][1], arr[i][3] + 1):
                color_map[j][k] += arr[i][4]
    #겹치는 면적 체크
    for i in range(10):
        for j in range(10):
            if color_map[i][j] == 3:
                result += 1
    print('#{} {}' .format(tc, result))