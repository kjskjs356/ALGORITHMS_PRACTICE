# 2490_윷놀이

arr = ['A', 'B', 'C', 'D', 'E']
result = []
for _ in range(3):
    tmp = list(map(int, input().split()))
    result.append(arr[tmp.count(0) - 1])
for i in range(3):
    print(result[i])