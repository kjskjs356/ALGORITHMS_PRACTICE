# 17140 이차원 배열과 연산


def rotate(arr):
    arr = list(map(list, zip(*arr)))
    return arr


def check(arr):
    row_len = len(arr)
    arr = rotate(arr)
    col_len = len(arr)
    arr = rotate(arr)
    if row_len >= col_len:
        return True, row_len
    else:
        return False, col_len


r, c, k = map(int, input().split())
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(3)]

# R연산인지, C연산인지 판단하기 위한 변수, 변수의 상태에 따라 배열을 뒤집어서 연산
is_R = True
t = 0
if r <= 2 and c <= 2 and board[r][c] == k:
    print(0)
else:
    while True:
        t += 1
        if t > 100:
            break
        is_R, len_arr = check(board)
        temp_arr = []
        max_len = 0
        if not is_R:
            board = rotate(board)
        for i in range(len_arr):
            num = dict()
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    continue
                if not num.get(board[i][j]):
                    num[board[i][j]] = 1
                else:
                    num[board[i][j]] += 1
            num_sort = sorted(num.items(), key = lambda x: (x[1], x[0]))
            temp = []
            for n in range(len(num_sort)):
                for m in range(2):
                    temp.append(num_sort[n][m])
            # 100개 이후로 커트
            temp_arr.append(temp[:100])
            if max_len < len(num_sort):
                max_len = len(num_sort)
        max_len *= 2
        if max_len > 100:
            max_len = 100
        # 각 행 or 열 별로 부족한 칸 만큼 0 추가
        for i in range(len_arr):
            now_len = len(temp_arr[i])
            if now_len < max_len:
                for _ in range(max_len - now_len):
                    temp_arr[i].append(0)
        board = temp_arr

        # 연산 끝나고 배열 뒤집혔으면 복원
        if not is_R:
            is_R = True
            len_arr, max_len = max_len, len_arr
            board = rotate(board)

        # A[r][c] == k 체크
        if r <= len_arr - 1 and c <= max_len - 1 and board[r][c] == k:
            break
    if t > 100:
        print(-1)
    else:
        print(t)