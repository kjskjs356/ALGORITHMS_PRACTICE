# 1764 듣보잡 풀이
#2022-08-09

N, M = map(int, input().split())
No_hear, No_see, Sum_arr = [], [], []
cnt = 0
for i in range(N):
    No_hear.append(input())
for i in range(M):
    No_see.append(input())
No_hear = set(No_hear)
No_see = set(No_see)
Sum_arr = No_hear & No_see
arr = sorted(Sum_arr)
print(arr)
print(len(Sum_arr))
for name in arr:
    print(name)