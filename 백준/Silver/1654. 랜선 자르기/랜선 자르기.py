# 1654 랜서자르기

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    # 중간 위치
    mid = (start + end) // 2
    # 랜선 수
    lines = 0
    for i in lan:
        # 분할 된 랜선 수
        lines += i // mid
    # 랜선의 개수가 분기점
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)