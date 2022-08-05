# 13736 사탕 분배 (미해결)

T = int(input())

for i in range(T):
    A, B, K = map(int, input().split())
    for _ in range(K):
        if A <= B:
            B -= A
            A *= 2
    print(f'#{i+1} {min(A, B)}')