# 2477 참외밭

N = int(input())
d_list = []
direction = {
    '1': 0, '2': 0, '3': 0, '4': 0,
}
area1 = area2 = 1
min_list = []

for _ in range(0, 6):
    direct, meter = map(int, input().split())
    d_list.append([direct, meter])
    direction[str(direct)] += 1

for i in range(len(d_list)):
    for key in direction.keys():
        if d_list[i][0] == int(key):
            if int(direction[key]) == 1:
                min_list.append(int(key))
                area1 *= d_list[i][1]

for i in range(len(d_list)):
    if i == (len(d_list) - 1):
        if not(d_list[0][0] in min_list or d_list[i - 1][0] in min_list):
            area2 *= d_list[i][1]
    elif not(d_list[i + 1][0] in min_list or d_list[i - 1][0] in min_list):
        area2 *= d_list[i][1]

print(N * (area1 - area2))