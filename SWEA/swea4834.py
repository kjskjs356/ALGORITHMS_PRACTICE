# 4834 cards 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    # 카드 장수
    N = int(input())
    # 카드 목록
    cards = input()
    card_arr = [0] * 10
    card_num = card_cnt = 0
    for n in cards:
        card_arr[int(n)] += 1
    # 장수가 많은 것 우선 => 장수 동일하면 큰 수 우선
    for i in range(N):
        if card_cnt <= card_arr[i]:
            if card_num <= i :
                card_num = i
                card_cnt = card_arr[i]
    print('#{} {} {}' .format(tc, card_num, card_cnt))