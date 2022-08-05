# 1712 손익분기점
A, B, C = map(int, input().split())
print(-1) if B >= C else print(A // (C - B) + 1)