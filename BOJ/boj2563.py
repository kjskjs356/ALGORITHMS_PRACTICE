# 2563 색종이

area = [[0 for x in range(100)] for y in range(100)]
Sum = 0
N = int(input())
square = []

for _ in range(N):
    square.append(list(map(int, input().split())))
#정사각형 하나씩 도화지에 붙이기
for i in range(N):
    for j in range(0, 10): # 가로
        for k in range(0, 10): # 세로
            area[square[i][0] + j][square[i][1]+ k] = 1

for i in range(len(area)):
    for j in range(len(area)):
        Sum += area[i][j]
print(Sum)
