# 25304 영수증

result = int(input())
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    result -= (a * b)
if result == 0:
    print('Yes')
else:
    print('No')