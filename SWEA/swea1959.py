#1959. 두 개의 숫자열
T = int(input())

for n in range(1, T+1):
    A_len, B_len = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Sum = 0
    
    if A_len > B_len:
        for i in range(0, A_len - B_len + 1):
            tmp = 0
            for j in range(0, B_len):
                tmp += A[j+i] * B[j]
            if Sum < tmp:
                Sum = tmp

    elif A_len < B_len:
        for i in range(0, B_len - A_len + 1):
            tmp = 0
            for j in range(0, A_len):
                tmp += A[j] * B[j+i]
            if Sum < tmp:
                Sum = tmp
    else:
        tmp = 0
        for i in range(0, A_len):
            tmp += A[i] * B[i]
        if Sum < tmp:
            Sum = tmp
    print(f'#{n} {Sum}')