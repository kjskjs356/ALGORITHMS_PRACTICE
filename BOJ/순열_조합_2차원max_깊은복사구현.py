# 순열 구현
def perm(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i, j in enumerate(arr):
        for k in perm(arr[:i] + arr[i + 1:], n - 1):
            result += [[j] + k]
    return result


arr = [0, 1, 2, 3, 4, 5]
print(perm(arr, 3))

# 조합 구현
def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


# yield를 사용한 조합 구현(좀 더 단순)
def comb2(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in comb2(arr[i + 1:], r - 1):
                yield [arr[i]] + j


# 중복 조합
def comb_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in comb_with_replacement(arr[i:], r - 1): # 이 부분(arr[i:])만 조합과 차이있음 !!
                yield [arr[i]] + j


# 중복 순열
def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in product(arr, r - 1): # arr[i:] 대신 arr 통째로 사용
                yield [arr[i]] + j


# 배열 90도 회전
def rotate_90(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = arr[r][c]
    return ret


# 배열 180도 회전
def rotate_180(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = arr[r][c]
    return ret


# 배열 -90도 회전
def rotate_270(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = arr[r][c]
    return ret


area = [[1, 2, 3, 4], [5, 6, 7, 8]]

# 2차원 배열 깊은 복사
new_area = [arr[:] for arr in area]

# 2차원 배열에서 max값 찾기
max_val = max(map(max, area))

arr = [[1,2,3],[4,5,6],[7,8,9]]

# 시계방향 회전 (한 줄)
arr = list(map(list, zip(*arr[::-1])))
for i in range(3):
    print(arr[i])
print()
# 반시계방향  (한 줄)
arr = [[1,2,3],[4,5,6],[7,8,9]]
arr = list(map(list, zip(*arr)))[::-1]
for i in range(3):
    print(arr[i])
print()

# 2차원 배열의 부분 회전
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

m, n = 2, 2
arr2 = list(map(list, zip(*[row[0:m] for row in arr[0:n]][::-1])))
for i in range(2):
    for j in range(2):
        arr[i][j] = arr2[i][j]
for i in range(4):
    print(arr[i])
print()