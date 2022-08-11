# 4837 부분집합의 합 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

arr = list(range(1, 13))
subset_arr = []
#1 ~ 12의 부분 집합 구하기
for i in range(1 << 12):
    subset= []
    for j in range(12):
        if i & (1 << j):
            subset.append(arr[j])
    subset_arr.append(subset)
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    #원소 N개인 부분 집합 중 합이 K인 리스트의 개수 체크
    for i in range(len(subset_arr)):
        if len(subset_arr[i]) == N:
            sum_arr = 0
            for j in subset_arr[i]:
                sum_arr += j
            if sum_arr == K:
                result += 1
    print('#{} {}' .format(tc, result))