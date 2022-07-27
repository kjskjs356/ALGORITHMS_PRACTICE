# 2559 수열

N, day = map(int, input().split())
temperature = list(map(int, input().split()))
tmp_sum = sum(temperature[0:day])
max_result = tmp_sum

for i in range(0, N - day):
    tmp_sum -= temperature[i]
    tmp_sum += temperature[i + day]
    if max_result < tmp_sum:
        max_result = tmp_sum
print(max_result)