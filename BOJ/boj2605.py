# 2605 줄세우기

N = int(input())
choice_num = list(map(int, input().split()))
wait_list = []

for i in range(N):
    if choice_num[i] == 0:
        wait_list.append(i + 1)
    else:
        wait_list.insert(-choice_num[i], i + 1)

for i in range(len(wait_list)):
    if i == len(wait_list) - 1:
        print(wait_list[i])
    else:
        print(wait_list[i], end = ' ')