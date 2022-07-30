# 1859_백만장자 프로젝트 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    result = 0

    # 사재기 시작
    while True:
        max_price = 0
        max_idx = 0
        sell_list = []
        for i in range(len(arr)):
            if max_price < arr[i]:
                max_price = arr[i]
                max_idx = i
        for i in range(max_idx + 1):
            if i == max_idx:
                result += arr[i] * i - sum(sell_list)
                del arr[:i + 1]
            else:
                sell_list.append(arr[i])
        if arr == [0]:
            break
    print('#{} {}' .format(tc, result))