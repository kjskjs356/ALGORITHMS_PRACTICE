# 2491 수열

N = int(input())
num_lst = list(map(int, input().split()))
print(num_lst)
max_count = 0
count = 2

for i in range(0, N - 1):
    if i == 0:
        continue
    if num_lst[i] >= num_lst[i - 1]:
        if num_lst[i + 1] >= num_lst[i]:
            count += 1
            if max_count < count:
                max_count = count
                print('1', count)
        else:
            count = 2

    if num_lst[i] <= num_lst[i - 1]:
        if num_lst[i + 1] <= num_lst[i]:
            count += 1
            print('2', count)
            if max_count < count:
                max_count = count
        else:
            count = 2
print(max_count)

