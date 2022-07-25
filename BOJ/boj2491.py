# 2491 수열

N = int(input())
num_lst = list(map(int, input().split()))
max_count = 1
d_count = u_count = 1
is_up = is_down = True

for i in range(1, N):
    if num_lst[i] > num_lst[i - 1]: # 현재 숫자가 전보다 큰 경우
        is_down = False
        d_count = 1
        if is_up == True:
            u_count += 1
            if max_count < u_count:
                max_count = u_count
        else:
            is_up = True
            u_count = 2
    elif num_lst[i] < num_lst[i - 1]: # 현재 숫자가 전보다 작은 경우
        is_up = False
        u_count = 1
        if is_down == True:
            d_count += 1
            if max_count < d_count:
                max_count = d_count
        else:
            is_down = True
            d_count = 2
    elif num_lst[i] == num_lst[i - 1]:# 값 똑같을 경우
        is_up = is_down = True
        u_count += 1
        d_count += 1
        if max_count < u_count:
            max_count = u_count
        if max_count < d_count:
            max_count = d_count

print(max_count)

