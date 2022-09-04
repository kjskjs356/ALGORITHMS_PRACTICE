# 18310 안테나

N = int(input())
locate = list(map(int, input().split()))
locate.sort()
result = 0
# 가장 가운데에 위치한 건물에 안테를 지어야 거리값이 최소가 되므로
# 간단하게 건물의 위치중 중간에 위치한 건물을 출력
print(locate[(N - 1) // 2])