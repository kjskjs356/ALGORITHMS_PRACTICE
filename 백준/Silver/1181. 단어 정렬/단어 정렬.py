# 1181 단어 정렬

N = int(input())
word = []
for _ in range(N):
    arr = input()
    word.append((arr, len(arr)))
word = list(set(word))
word.sort(key=lambda x : (x[1], x[0]))
for i in range(len(word)):
    print(word[i][0])