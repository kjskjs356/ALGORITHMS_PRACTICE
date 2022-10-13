from collections import deque

area = [deque([1,2,3]),deque([4,5,6])]
for i in range(len(area)):
    print(area[i])
area2 = deque(map(list, zip*(area)[::-1]))
area[0][0] = 0
print(area)
print(area2)