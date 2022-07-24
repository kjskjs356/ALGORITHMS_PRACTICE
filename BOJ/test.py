
a= [1, 4, 3, 2, 5, 6]

num = [i for i in range(len(a[:3])) if a[i] == 1]
a.insert(2, a.pop())
print(a)