# 1302 베스트 셀러

N = int(input())

book = dict()
for _ in range(N):
    name = input()
    if not book.get(name):
        book[name] = 1
    else:
        book[name] += 1
sorted_book = sorted(book.items(), key=lambda x: (-x[1], x[0]))
print(sorted_book[0][0])