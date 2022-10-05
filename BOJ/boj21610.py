# 마법사 상어와 비바라기 풀이

# 9시 방향부터 시계방향(총 8방향)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1 -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    d, s = map(int, input().split())
    # 최초 구름 생성
