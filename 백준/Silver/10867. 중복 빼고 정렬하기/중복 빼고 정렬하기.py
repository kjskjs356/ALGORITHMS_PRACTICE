# 10867 중복 빼고 정렬하기
N = int(input())
arr = list(set(list(map(int, input().split()))))
arr.sort()
print(' '.join(map(str, arr)))