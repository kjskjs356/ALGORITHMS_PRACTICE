# 2525 오븐 시계

h, m = map(int, input().split())
time = int(input())
if time + m >= 60:
    h += (time + m) // 60
    m = (time + m) % 60
else:
    m += time
if h>= 24:
    h -= 24
print(h, m)