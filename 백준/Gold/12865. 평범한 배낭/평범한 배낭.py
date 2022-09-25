# 평범한 배낭 풀이

N, K = map(int, input().split())
# 0: 무게, 1: 가치
item = [list(map(int, input().split())) for _ in range(N)]
bags = [0] * (K + 1)
for i in range(N):
    # 최대치보다 무거우면 패스
    if item[i][0] > K:
        continue
    for j in range(K, 0, -1):
        # 가방 인덱스를 역 순으로 순회하면서 각 경우의 수에 현 인덱스의 물건이 들어갔을 경우
        # 무게가 범위 내에 있을때 비교 + 0번째 인덱스는 별도로 비교
        if item[i][0] + j <= K and bags[j] != 0:
            bags[j + item[i][0]] = max(bags[j + item[i][0]], bags[j] + item[i][1])
    # 현재 인덱스의 물건을 넣었을 경우의 무게에 해당하는 가치와 기존에 존재했던 해당 무게에 대한 가치 비교
    bags[item[i][0]] = max(bags[item[i][0]], item[i][1])
print(max(bags))