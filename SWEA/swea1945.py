# 1945 간단한 소인수 분해 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    #각 소인수로 더이상 나누어지지 않을때까지 나눗셈 시행
    while True:
        if N % 2 == 0:
            N //= 2
            a += 1
        elif N % 3 == 0:
            N //= 3
            b += 1
        elif N % 5 == 0:
            N //= 5
            c += 1
        elif N % 7 == 0:
            N //= 7
            d += 1
        elif N % 11 == 0:
            N //= 11
            e += 1
        else:
            break
    print('#{} {} {} {} {} {}' .format(tc + 1, a, b, c, d, e))