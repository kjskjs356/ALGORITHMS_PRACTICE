# 4831 electric_bus 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
	# k : 최대 이동 가능한 정류장 수
	# n : 종점 번호 (0부터)
	# m : 충전기 설치된 정류장 수
	# bus_stop : 충전기 설치된 버스 정류장 리스트
    k, n, m = map(int, input().split())
    bus_stop = [0] * (n + 1)
    result = 0
    breaker = False
    charge_cnt = 0
    charge = list(map(int, input().split()))
    for x in charge:
        bus_stop[x] = 1
    #현재 위치 체크
    now_stop = 0
    check = 0
    #버스가 한번에 최대 몇 번 정류장까지 갈 수 있는지 확인 후 위치 갱신 + 충전 횟수 카운트(종점까지 반복)
    while True:
        if breaker: break
        charge_cnt = 0
        for i in range(1, k + 1):
            #종점 도착하면 루프 탈출
            if now_stop + i >= n:
                breaker = True
                break
            if bus_stop[now_stop + i] == 1:
                check = now_stop + i
                charge_cnt += 1
        #for문이 끝날때마다 가장 멀리 도착할 수 있는 정류장 번호 카운트
        now_stop = check
        #종점 도착하면 결과값 +1 없이 루프 탈출
        if breaker: break
        result += 1
        #한 번 충전으로 이동 거리 모자르면 0 반환
        if charge_cnt == 0:
            result = 0
            break
    print('#{} {}' .format(tc, result))