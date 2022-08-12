# 1213_string 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    find_str = input()
    str_arr = input()
    i = 0
    cnt = 0
    idx = 0
    #인덱스가 증가할때마다 카운팅 함으로써 개수 계산
    while True:
        tmp = str_arr.find(find_str, i)
        if idx < tmp:
            cnt += 1
            idx = tmp
        if tmp == -1:
            break
        i += 1
    print('#{} {}' .format(tc, cnt))