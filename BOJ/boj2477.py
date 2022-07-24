# 2477 참외밭

N = int(input())
d_list = []

for _ in range(0, 6):
    direct, meter = map(int, input().split())
    d_list.append([meter, direct])

print(d_list)
d_list2 = sorted(d_list)
max_h = d_list2[5][0]
max_w = d_list2[4][0]
max_area = max_h * max_w

for i in range(len(d_list)):
    if d_list[i][0] == max_h or d_list[i][0] == max_w:
        continue