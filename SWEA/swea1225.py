# 1225 암호생성기

for n in range(10):
    num = int(input())
    pwd = list(map(int, input().split()))
    breaker =False

    while True:
        if breaker == True:
            break
        for i in range(5):
            tmp = pwd.pop(0) - (i + 1)
            if tmp < 0:
                pwd.append(0)
            else:
                pwd.append(tmp)
            if pwd[-1] == 0:
                breaker = True
                break
    print(f'#{n + 1}', end=' ')
    for i in range(len(pwd)):
        if i == len(pwd) - 1:
            print(pwd[i])
        else:
            print(pwd[i], end=' ')