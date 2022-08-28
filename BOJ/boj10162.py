# 10162 전자레인지 풀이

T = int(input())
#각각 5분 1분 10초
button = [0, 0, 0]
Flag = False
while T > 0:
    if T // 300 > 0:
        button[0] += T // 300
        T %= 300
    elif T // 60 > 0:
        button[1] += T // 60
        T %= 60
    elif T // 10 > 0:
        button[2] += T // 10
        T %= 10
    else:
        Flag = True
        break
if Flag:
    print(-1)
else:
    print(*button)