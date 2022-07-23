# 2304 창고 다각형

N = int(input())
pole = []
difference = 0
max_height = 0
max_num = 0
area1 = area2 = 0 # 좌 우 넓이

def pole_area(width, height):
    area = width * height
    return area

for _ in range(N):
    location, height = map(int, input().split())
    pole.append([location, height])
pole_sort = sorted(pole)

for i in range(len(pole_sort)):
    if max_height <= pole_sort[i][1]:
        max_height = pole_sort[i][1]
        max_num = i

# 왼쪽에서 높은 곳 까지탐색
left_height = pole_sort[0][1]
left_width = pole_sort[0][0]
for i in range(1, max_num + 1):
    if left_height <= pole_sort[i][1]:
        area1 += pole_area(pole_sort[i][0] - left_width, left_height)
        left_width = pole_sort[i][0]
        left_height= pole_sort[i][1]
    else:
        continue

# 오른쪽에서 높은 곳까지 탐색
right_height = pole_sort[-1][1]
right_width = pole_sort[-1][0]
for i in range(2, len(pole_sort) - max_num + 1):
    if right_height <= pole_sort[-i][1]:
        area2 += pole_area(right_width - pole_sort[-i][0], right_height)
        right_width = pole_sort[-i][0]
        right_height= pole_sort[-i][1]
    else:
        continue
result = area1 + area2 + max_height
print(result)