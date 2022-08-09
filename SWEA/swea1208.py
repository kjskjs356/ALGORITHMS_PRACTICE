# 1208 flatten 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')
#최대 높이와 최소 높이를 탐색해서 1씩 교환하는 함수
def flatten(arr):
    max_height = 0
    min_height = arr[0]
    for i in range(100):
        if max_height < arr[i]:
            max_height = arr[i]
        if min_height > arr[i]:
            min_height = arr[i]
    for i in range(100):
        if arr[i] == max_height:
            arr[i] -= 1
            break
    for i in range(100):
        if arr[i] == min_height:
            arr[i] += 1
            break
    return arr

def max_arr(arr):
    result = 0
    for x in arr:
        if result < x:
            result = x
    return result

def min_arr(arr):
    result = arr[0]
    for x in arr:
        if result > x:
            result = x
    return result

for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    #dump 횟수만큼 루프
    while dump > 0:
        arr = flatten(arr)
        dump -= 1
    result = max_arr(arr) - min_arr(arr)
    print('#{} {}' .format(tc, result))

