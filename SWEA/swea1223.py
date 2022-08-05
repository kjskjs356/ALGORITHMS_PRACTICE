# 1223 계산기2

N= int(input())
exp = input()
result = []
tmp = []
Sum = 0

for n in range(10):
    for i in range(len(exp)):
        if i % 2 == 0:
            tmp.append(int(exp[i]))
            print(tmp)
        else:
            if exp[i] == '+':
                for x in tmp:
                    Sum *= x
                result.append(Sum)
                Sum = 0
                tmp = []
            else:
                continue
    print(f'#{n+1} {sum(result)}')