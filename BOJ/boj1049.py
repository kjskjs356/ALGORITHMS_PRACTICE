# 1049 기타줄 풀이

N, M = map(int, input().split())
price1 = []
result = 0
for _ in range(M):
    #패키지가격 , 낱개가격
    price1.append(list(map(int, input().split())))
#패키지 가격 중 제일 싼것 부터 선택하기 위해 오름차순 정렬
price1.sort()
#낱개 가격 기준 오름차순 배열 생성
price2 = sorted(price1, key=lambda x:x[1])
while N > 0:
    #남은 개수 확인(세트 구매 위해 6개이상 여부)
    if N >= 6:
        #6개 이상이면 패키지가격이 낱개보다 싼 지 체크
        if price1[0][0] < 6 * price2[0][1]:
            result += N // 6 * price1[0][0]
            N %= 6
        else:
            result += N * price2[0][1]
            N = 0
    #N개 미만
    else:
        if price1[0][0] < N * price2[0][1]:
            result += price1[0][0]
            N = 0
        else:
            result += N * price2[0][1]
            N = 0
print(result)