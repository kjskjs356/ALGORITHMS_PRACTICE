# 14888 연산자 끼워넣기
# 최댓값, 최솟값 둘 다 구해야함


def cal(num1, num2, op):
    ops = {
        0: lambda x, y: x+y,
        1: lambda x, y: x-y,
        2: lambda x, y: x*y,
        3: lambda x, y: x//y if x >= 0 else (abs(x)//y) * -1
    }
    return ops[op](num1, num2)


def back(now, idx):
    global max_ans, min_ans
    # 연산이 끝나면 판별
    if sum(operator) == 0:
        max_ans = max(max_ans, now)
        min_ans = min(min_ans, now)
        return
    for i in range(idx, len(area)):
        for j in range(len(operator)):
            if operator[j] > 0:
                operator[j] -= 1
                back(cal(now, area[i], j), i + 1)
                operator[j] += 1



N = int(input())
area = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_ans, min_ans = -float('inf'), float('inf')
back(area[0], 1)
print(max_ans)
print(min_ans)