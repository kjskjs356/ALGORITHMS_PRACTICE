# 10773 제로

N = int(input())
num_list =[]
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(num_list) != 0:
            num_list.pop()
        else:
            num_list.append(num)
    else:
        num_list.append(num)
if not num_list:
    print(0)
else:
    print(sum(num_list))