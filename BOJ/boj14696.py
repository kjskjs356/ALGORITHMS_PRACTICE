# 14696 딱지놀이

# 라운드 수
N = int(input())
result = []
for _ in range(N):
    # a학생이 낸 카드 수 + 종류
    a = list(map(int, input().split()))
    a.pop(0)
    a.sort(reverse=True)
    # b학생이 낸 카드 수 + 종류
    b = list(map(int, input().split()))
    b.pop(0)
    b.sort(reverse=True)
    #볕부터 순서대로 체크
    if a.count(4) > b.count(4):
        result.append('A')
    elif a.count(4) < b.count(4):
        result.append('B')
    else:
        if a.count(3) > b.count(3):
            result.append('A')
        elif a.count(3) < b.count(3):
            result.append('B')
        else:
            if a.count(2) > b.count(2):
                result.append('A')
            elif a.count(2) < b.count(2):
                result.append('B')
            else:
                if a.count(1) > b.count(1):
                    result.append('A')
                elif a.count(1) < b.count(1):
                    result.append('B')
                else:
                    result.append('D')
for i in range(N):
    print(result[i])