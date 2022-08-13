# 13994_새로운 버스 노선 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_arr = []
    for _ in range(N):
        bus_arr.append(list(map(int, input().split())))
    bus_stop = [0] * 1001
    result = 0
    for i in range(N):
            #일반 버스
            if bus_arr[i][0] == 1:
                for j in range(bus_arr[i][1], bus_arr[i][2] + 1):
                    bus_stop[j] += 1
            #급행 버스
            elif bus_arr[i][0] == 2:
                #출발점 짝수인 경우
                if bus_arr[i][1] % 2 == 0:
                    for j in range(bus_arr[i][1], bus_arr[i][2] + 1, 2):
                        bus_stop[j] += 1
                    if bus_arr[i][2] % 2 == 1: bus_stop[bus_arr[i][2]] += 1
                else:
                    for j in range(bus_arr[i][1], bus_arr[i][2] + 1, 2):
                        bus_stop[j] += 1
                    if bus_arr[i][2] % 2 == 0: bus_stop[bus_arr[i][2] ] += 1
            #광역 버스
            elif bus_arr[i][0] == 3:
                #출발점 짝수
                if bus_arr[i][1] % 2 == 0:
                    for j in range(bus_arr[i][1], bus_arr[i][2] + 1):
                        if j % 4 == 0:
                            bus_stop[j] += 1
                    if bus_arr[i][1] % 4 != 0: bus_stop[bus_arr[i][1]] += 1
                    if bus_arr[i][2] % 4 != 0: bus_stop[bus_arr[i][2]] += 1
                #출발점 홀수
                if bus_arr[i][1] % 2 == 1:
                    for j in range(bus_arr[i][1], bus_arr[i][2] + 1):
                        if j % 3 == 0 and j % 10 != 0:
                            bus_stop[j] += 1
                    if not (bus_arr[i][1] % 3 == 0 and bus_arr[i][1] % 10 != 0): bus_stop[bus_arr[i][1]] += 1
                    if not (bus_arr[i][2] % 3 == 0 and bus_arr[i][2] % 10 != 0): bus_stop[bus_arr[i][2]] += 1
    for i in range(len(bus_stop)):
        if result < bus_stop[i]:
            result = bus_stop[i]
    print('#{} {}' .format(tc, result))