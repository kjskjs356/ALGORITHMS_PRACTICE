area = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
area2 = [arr[:] for arr in area]
area[0][0][1] = 2
for i in range(4):
    print(area[i])
print()
for i in range(4):
    print(area2[i])
print()
print(sum(area))