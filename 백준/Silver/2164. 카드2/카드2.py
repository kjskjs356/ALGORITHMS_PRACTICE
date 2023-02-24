from collections import deque
n = int(input())
data = deque([])
for i in range(n):
    data.append(i+1)

while len(data) != 1:
    data.popleft()
    tmp = data.popleft()
    data.append(tmp)

print(data[0])