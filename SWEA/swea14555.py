# 14555 공과 잡초

T = int(input())
for n in range(T):
    cnt = 0
    field = input()
    for i in range(len(field)):
        if field[i] == '(':
            cnt += 1
        elif field[i] == ')':
            if field[i - 1] == '(':
                continue
            else:
                cnt += 1
    print(f'#{n+1} {cnt}')
