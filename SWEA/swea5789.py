# 5789 현주의 상자 바꾸기 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N
    L = []
    R = []
    for i in range(Q):
        #L, R 범위 리스트로 저장
        L_input, R_input = map(int, input().split())
        L.append(L_input)
        R.append(R_input)
    #범위에 따라 숫자 부여
    for i in range(Q):
        for j in range(L[i] - 1, R[i]):
            box[j] = i + 1
    print('#{}'. format(tc), end=' ')
    for i in range(N):
        if i != N - 1:
            print(box[i], end=' ')
        else:
            print(box[i])