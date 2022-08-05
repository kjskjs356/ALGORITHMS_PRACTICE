# 1223 계산기2

for n in range(10):
    N= int(input())
    exp = input()
    result = []
    tmp = []
    Sum = 1
    for i in range(N):
        if i % 2 == 0:
            tmp.append(int(exp[i]))
            if i == len(exp) - 1:
                for x in tmp:
                    Sum *= x
                result.append(Sum)
        else:
            if exp[i] == '+':
                for x in tmp:
                    Sum *= x
                result.append(Sum)
                Sum = 1
                tmp = []
            else:
                continue
    print(f'#{n+1} {sum(result)}')
    result = []