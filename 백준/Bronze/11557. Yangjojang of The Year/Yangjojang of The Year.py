# 11557 Yangjojang of The Year

T = int(input())
univ = dict()
ans = ''

for _ in range(T):
    N = int(input())
    for _ in range(N):
        name, num = map(str, input().split())
        if not univ.get(name):
            univ[name] = int(num)
        else:
            univ[name] += int(num)
    cnt = 0
    for k, v in univ.items():
        if cnt < v:
            cnt = v
            ans = k
    print(ans)