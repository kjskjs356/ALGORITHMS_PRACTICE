# 1231_중위순회 문제풀이
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')

def inorder(n):
    if n:
        inorder(ch1[n])
        print(word[n], end='')
        inorder(ch2[n])

for tc in range(1, 11):
    N = int(input())
    E = N - 1
    word = ['']
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for i in range(1, N + 1):
        arr = input().split()
        word.append(arr[1])
        if len(arr) >= 3:
            ch1[int(arr[0])] = int(arr[2])
        if len(arr) >= 4:
            ch2[int(arr[0])] = int(arr[3])
    print('#{}'. format(tc), end=' ')
    inorder(1)
    print()