# 6485 삼성시의 버스 노선 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = []
    B = []
    C = []
    for i in range(N):
        A_no, B_no = map(int, input().split())
        A.append(A_no)
        B.append(B_no)
    P = int(input())
    for _ in range(P):
        C.append(int(input()))
    C_cnt = [0] * P
    #각 버스 별 이용하는 정류장 체크
    for i in range(P):
        for j in range(N):
            if A[j] <= C[i] <= B[j]:
                C_cnt[i] += 1
            else:
                continue
    print('#{}' .format(tc), end=' ')
    for i in range(P):
        if i != P - 1 :
            print(C_cnt[i], end=' ')
        else:
            print(C_cnt[i])
