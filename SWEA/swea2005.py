# 2005_파스칼 삼각형 풀이
# 2022-08-17

import sys
sys.stdin = open('input.txt', 'r')

def pascal(idx, N):
    if idx == N:
        return arr
    elif idx == 0:
        arr.append([1])
        idx += 1
        pascal(idx, N)
        return arr
    elif idx == 1:
        arr.append([1, 1])
        idx += 1
        pascal(idx, N)
        return arr
    # 3번 째 줄이상
    else:
        tmp = [1, 1]
        for i in range(1, idx):
            tmp.insert(i, arr[idx - 1][i - 1] + arr[idx - 1][i])
        arr.append(tmp)
        idx += 1
        pascal(idx, N)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    result = pascal(0, N)
    print('#{}' .format(tc))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

