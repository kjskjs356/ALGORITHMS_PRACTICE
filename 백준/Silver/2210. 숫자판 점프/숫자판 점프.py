# 2210 숫자판 점프


def back(x, y, num, num_list):
    if len(num) == 6:
        if not num in num_list:
            num_list.append(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            back(nx, ny, num + str(board[nx][ny]), num_list)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = [list(map(int, input().split())) for _ in range(5)]
num_list = []
for i in range(5):
    for j in range(5):
        visited = [[False for _ in range(5)] for _ in range(5)]
        visited[i][j] = True
        number = ''
        number += str(board[i][j])
        back(i,  j, number, num_list)
print(len(num_list))