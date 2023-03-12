# 2580 스도쿠


def back(x, y, cnt):
    global escape
    if escape:
        return
    if cnt == 0:
        escape = True
        return
    if board[x][y] == 0:
        # 넣을 수 있는 숫자 우선 넣기
        for n in range(1, 10):
            breaker = False
            # 가로 체크
            if n in board[x]:
                continue
            # 세로 체크
            for j in range(9):
                if n == board[j][y]:
                    breaker = True
                    break
            if breaker:
                continue
            # 블럭 설정
            a, b = x // 3, y // 3
            for i in range(a * 3, a * 3 + 3):
                if breaker:
                    break
                for j in range(b * 3, b * 3 + 3):
                    if n == board[i][j]:
                        breaker = True
                        break
            if breaker:
                continue
            board[x][y] = n
            if y < 8:
                back(x, y + 1, cnt - 1)
                if escape:
                    return
                board[x][y] = 0
            else:
                back(x + 1, 0, cnt - 1)
                if escape:
                    return
                board[x][y] = 0
    else:
        if y < 8:
            back(x, y + 1, cnt)
            if escape:
                return
        else:
            back(x + 1, 0, cnt)
            if escape:
                return

cnt = 0
board = []
for _ in range(9):
    arr = list(map(int, input().split()))
    for i in range(9):
        if arr[i] == 0:
            cnt += 1
    board.append(arr)
escape = False
back(0, 0, cnt)
for i in range(9):
    print(' '.join(map(str, board[i])))
