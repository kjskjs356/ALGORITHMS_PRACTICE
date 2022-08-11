# 4839 이진탐색 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int,input().split())
    page = range(1, P + 1)
    first_A, end_A = page[0], page[-1]
    first_B, end_B = page[0], page[-1]
    Fa, Fb = False, False
    while True:
        if Fa or Fb:
            break
        #A 이진탐색
        if (first_A + end_A) // 2 == Pa:
            Fa = True
        else:
            if (first_A + end_A) // 2 > Pa:
                end_A = (first_A + end_A) // 2
            else:
                first_A = (first_A + end_A) // 2
        #B 이진탐색
        if (first_B + end_B) // 2 == Pb:
            Fb = True
        else:
            if (first_B + end_B) // 2 > Pb:
                end_B = (first_B + end_B) // 2
            else:
                first_B = (first_B + end_B) // 2
        #둘 다 찾는게 불가능 할 경우 or 비길 경우 탈출
        if first_A == 999 and end_B == 1:
            break
    print('#{}' .format(tc), end=' ')
    if Fa and not Fb:
        print('A')
    elif not Fa and Fb:
        print('B')
    else:
        print(0)