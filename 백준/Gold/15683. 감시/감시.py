# 15683 감시


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
min_num = float("inf")


def one_cctv(r, c, visited, flag):  # 1번 씨씨티비 감시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        nx = r + dx[flag]
        ny = c + dy[flag]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                break
            if visited[nx][ny] <= 0:
                visited[nx][ny] -= 1
            r, c = nx, ny
        else:
            break


def one_cctv_clear(r, c, visited, flag):  # 1번 씨시티비가 감시했던 장소들을 다시 원래대로
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        nx = r + dx[flag]
        ny = c + dy[flag]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                break
            if visited[nx][ny] < 0:
                visited[nx][ny] += 1
            r, c = nx, ny
        else:
            break


def two_cctv(r, c, visited, flag):
    dx = [(0, 0), (-1, 1)]
    dy = [(-1, 1), (0, 0)]
    tr, tc = r, c
    for i in range(2):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:  # 계쏙 범위 안에 있나
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r, c = nx, ny
            else:
                break  # 계속 더하기 때문에 범위 안에 계속 있을 수가 없어


def two_cctv_clear(r, c, visited, flag):  # 2번 씨시티비가 감시했던 장소들을 다시 원래대로
    dx = [(0, 0), (-1, 1)]
    dy = [(-1, 1), (0, 0)]
    tr, tc = r, c
    for i in range(2):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r, c = nx, ny
            else:
                break


def three_cctv(r, c, visited, flag):
    dx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tr, tc = r, c
    for i in range(2):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r, c = nx, ny
            else:
                break


def three_cctv_clear(r, c, visited, flag):  # 3번 씨시티비가 감시했던 장소들을 다시 원래대로
    dx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tr, tc = r, c
    for i in range(2):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r, c = nx, ny
            else:
                break


def four_cctv(r, c, visited, flag):  # 4번 씨씨티비 감시
    dx = [(0, -1, 0), (-1, 0, 1), (0, 1, 0), (1, 0, -1)]
    dy = [(-1, 0, 1), (0, 1, 0), (1, 0, -1), (0, -1, 0)]
    tr, tc = r, c
    for i in range(3):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r, c = nx, ny
            else:
                break


def four_cctv_clear(r, c, visited, flag):  # 4 번 씨시티비가 감시했던 장소들을 다시 원래대로
    dx = [(0, -1, 0), (-1, 0, 1), (0, 1, 0), (1, 0, -1)]
    dy = [(-1, 0, 1), (0, 1, 0), (1, 0, -1), (0, -1, 0)]
    tr, tc = r, c
    for i in range(3):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r, c = nx, ny
            else:
                break


def five_cctv(r, c, visited, flag):  # 5번 씨씨티비 감시
    dx = [(0, -1, 0, 1)]
    dy = [(-1, 0, 1, 0)]
    tr, tc = r, c
    for i in range(4):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] <= 0:
                    visited[nx][ny] -= 1
                r, c = nx, ny
            else:
                break


def five_cctv_clear(r, c, visited, flag):  # 5번 씨시티비가 감시했던 장소들을 다시 원래대로
    dx = [(0, -1, 0, 1)]
    dy = [(-1, 0, 1, 0)]
    tr, tc = r, c
    for i in range(4):
        r, c = tr, tc
        while True:
            nx = r + dx[flag][i]
            ny = c + dy[flag][i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 6:  # 벽이라면 바로 탈출
                    break
                if visited[nx][ny] < 0:
                    visited[nx][ny] += 1
                r, c = nx, ny
            else:
                break


def solve(r, c, data):
    global min_num
    if c == M:  # 맨 오른쪽 까지 왔다면 한 줄 밑으로
        c = 0
        r += 1
    if r == N:  # 행이 범위를 벗어났다면 사각지대 최소 갯수 구하고 리턴
        count = 0
        for i in range(N):
            for j in range(M):
                if data[i][j] == 0:
                    count += 1
        min_num = min(min_num, count)
        return
    if 1 <= data[r][c] <= 5:  # 씨씨티비가 있는 장소라면 해당 번호에 맞게 함수 호출
        if data[r][c] == 1:
            one_cctv(r, c, data, 0)  # 씨시티비로 감시하고
            solve(r, c + 1, data)  # 다음 열로 재귀함수 부르고
            one_cctv_clear(r, c, data, 0)  # 다시 돌아왔을 때는 원래대로 되돌리기
            one_cctv(r, c, data, 1)  # 다음 방향으로 다시 감시
            solve(r, c + 1, data)
            one_cctv_clear(r, c, data, 1)
            one_cctv(r, c, data, 2)
            solve(r, c + 1, data)
            one_cctv_clear(r, c, data, 2)
            one_cctv(r, c, data, 3)
            solve(r, c + 1, data)
            one_cctv_clear(r, c, data, 3)
        if data[r][c] == 2:
            two_cctv(r, c, data, 0)
            solve(r, c + 1, data)
            two_cctv_clear(r, c, data, 0)
            two_cctv(r, c, data, 1)
            solve(r, c + 1, data)
            two_cctv_clear(r, c, data, 1)
        if data[r][c] == 3:
            three_cctv(r, c, data, 0)
            solve(r, c + 1, data)
            three_cctv_clear(r, c, data, 0)
            three_cctv(r, c, data, 1)
            solve(r, c + 1, data)
            three_cctv_clear(r, c, data, 1)
            three_cctv(r, c, data, 2)
            solve(r, c + 1, data)
            three_cctv_clear(r, c, data, 2)
            three_cctv(r, c, data, 3)
            solve(r, c + 1, data)
            three_cctv_clear(r, c, data, 3)
        if data[r][c] == 4:
            four_cctv(r, c, data, 0)
            solve(r, c + 1, data)
            four_cctv_clear(r, c, data, 0)
            four_cctv(r, c, data, 1)
            solve(r, c + 1, data)
            four_cctv_clear(r, c, data, 1)
            four_cctv(r, c, data, 2)
            solve(r, c + 1, data)
            four_cctv_clear(r, c, data, 2)
            four_cctv(r, c, data, 3)
            solve(r, c + 1, data)
            four_cctv_clear(r, c, data, 3)
        if data[r][c] == 5:
            five_cctv(r, c, data, 0)
            solve(r, c + 1, data)
            five_cctv_clear(r, c, data, 0)
    else:  # 씨씨티비가 없던 좌표였다면 다음 좌표로 이동
        solve(r, c + 1, data)


solve(0, 0, data)
print(min_num)