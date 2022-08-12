# 1221_GNS 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T + 1):
    case, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    result = []

    for i in range(len(num_list)):
        for j in range(len(arr)):
            if arr[j] == num_list[i]:
                result.append(arr[j])
    print('#{}' .format(tc))
    for idx in result:
        print(idx, end=' ')
    print()