n, m = 10, 10

mylist = [[1]*m for _ in range(n)]

newlist=[(i,j) for i in range(n) for j in range(m) if mylist[i][j]==1]
print(newlist)