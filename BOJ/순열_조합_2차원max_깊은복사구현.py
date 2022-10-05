# 순열 구현
def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for x in arr:
            result.append([x])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n - 1):
                result.append([arr[i]] + p)
    return result


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


area = [[1, 2, 3, 4], [5, 6, 7, 8]]

# 2차원 배열 깊은 복사
new_area = [arr[:] for arr in area]

# 2차원 배열에서 max값 찾기
max_val = max(map(max, area))

