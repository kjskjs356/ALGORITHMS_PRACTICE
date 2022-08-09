# 5430 AC 풀이

T = int(input())
for tc in range(T):
    p = input()
    n = int(input())
    arr = list(input())
    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue
    arr.pop(0)
    arr.pop(-1)
    arr = ''.join(arr)
    arr = list(map(int, arr.split(',')))
    r_cnt = 0
    if p.count('D') > len(arr):
        print('error')
        continue
    elif p.count('D') == len(arr):
        print('[]')
        continue
    for i in range(len(p)):
        if p[i] == 'R':
            r_cnt += 1
        elif p[i] == 'D':
            if r_cnt % 2 == 0:
                arr.pop(0)
            else:
                arr.pop(-1)
    print('[', end='')
    for i in range(len(arr)):
        if r_cnt % 2:
            if i == len(arr) - 1:
                print(arr[-(i + 1)], end='')
            else:
                print(arr[-(i + 1)], end=',')
        else:
            if i == len(arr) - 1:
                print(arr[i], end='')
            else:
                print(arr[i], end=',')
    print(']')