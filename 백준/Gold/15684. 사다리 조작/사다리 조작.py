# 15684 사다리 조작

# N : 세로선의 개수, M : 가로선의 개수, H : 가로선을 놓을 수 있는 위치의 개수


def check():
    for num in range(N):
        idx = num
        for j in range(H):
            if board[j][idx]:
                idx += 1
            elif idx > 0 and board[j][idx - 1]:
                idx -= 1
        if idx != num:
            return False
    return True


def back(cnt, x, y):
    global ans
    if check():
        ans = min(cnt, ans)
        return
    elif cnt == 3 or cnt >= ans:
        return
    for i in range(x, H):
        if i == x:
            idx = y
        else:
            idx = 0
        for j in range(idx, N - 1):
            if not board[i][j] and not board[i][j + 1]:
                if j > 0 and board[i][j - 1]: continue
                board[i][j] = True
                back(cnt + 1, i, j+ 2)
                board[i][j] = False


N, M, H = map(int, input().split())
board = [[False] * N for _ in range(H)]
ans = 0

if M == 0:
    print(0)
else:
    for _ in range(M):
        # a: 세로선의 a번 위치, b: 세로선 번호
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        board[a][b] = True
    # 사다리 추가없이 우선 시행
    if check():
        print(0)
    else:
        ans = 4
        back(0, 0, 0)
        if ans < 4:
            print(ans)
        else:
            print(-1)