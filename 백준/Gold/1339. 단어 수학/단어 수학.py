# 1339 단어 수학
# 잘못된 논리로 인해 코드 리셋...
# 중요도를 이용하여 푸는 문제

N = int(input())
word = [input() for _ in range(N)]
ans = 0

# 총 26개의 알파벳 A ~ Z
alpha = [0 for _ in range(26)]
for w in word:
    i = 0
    while w:
        first = w[-1]
        # ord를 이용해서 해당 글자에 맞는 알바펫 인덱스에 10 제곱수로 계산(pow)
        alpha[ord(first) - ord('A')] += pow(10, i)
        # 연산 자릿수 1씩 증가(1, 10, 100, 1000, ...)
        i += 1
        # 단어의 자릿수를 하나씩 줄여가면서 w의 최고 차수까지 반복
        w = w[:-1]

alpha.sort(reverse=True)
for i in range(9, 0, -1):
    ans += i * alpha[9 - i]
print(ans)