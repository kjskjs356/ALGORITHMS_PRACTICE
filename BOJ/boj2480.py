# 2480 주사위 세개

d1, d2, d3 = map(int, input().split())
result = 0
# 같은 눈 3개
if d1 == d2 == d3:
    result += 10000 + d1 * 1000
#같은 눈 2개
elif d1 == d2 or d1 == d3:
    result += 1000 + d1 * 100
elif d2 == d3:
    result += 1000 + d2 * 100
else:
    result = max(d1, d2, d3) * 100
print(result)