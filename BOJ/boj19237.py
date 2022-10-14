# 어른 상어 풀이

""""
상어가 움직이고자 하는 방향 중 빈칸이 있다면 빈칸 우선순위로 이동
빈칸이 없으면 자신의 냄새가 있는 칸 중 우선순위가 높은 칸으로 이동
같은 칸에 존재하는 상어를 식별하기 위해 이동이 끝난 후 냄새 남기기
"""


def smell_update():
    # 기존 냄새 갱신& 현 상어 위치에 새로운 냄새 남기기
    for x in range(N):
        for y in range(N):
            if shark_smell[x][y][1] > 0:
                shark_smell[x][y][1] -= 1
                if shark_smell[x][y][1] == 0:
                    shark_smell[x][y] = [0, 0]
            if area[x][y] > 0:
                shark_smell[x][y][0] = area[x][y]
                shark_smell[x][y][1] = k



def shark_move():
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            # 상어 존재 여부확인
            if area[x][y] > 0 and not visited[x][y]:
                # 상어의 번호(1번 => 인덱스 0)
                num = area[x][y] - 1
                is_move = False
                # 상어가 이동할 위치 중 빈칸 여부 부터 체크
                for i in range(4):
                    nx = x + dx[shark_priority[num][shark_direct[num] - 1][i] - 1]
                    ny = y + dy[shark_priority[num][shark_direct[num] - 1][i] - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        # 이동 가능한 빈칸이 존재
                        if shark_smell[nx][ny] == [0, 0]:
                            area[x][y] = 0
                            is_move = True
                            visited[nx][ny] = True
                            shark_direct[num] = shark_priority[num][shark_direct[num] - 1][i]
                            # 이동만 하고 냄새는 아직 X (중복 상어 여부 체크 위해)
                            # 현재 상어보다 번호 높은 상어가 있으면 현재 상어로 갱신
                            if area[nx][ny] > num + 1 or area[nx][ny] == 0:
                                area[nx][ny] = num + 1
                            break
                # 이동 가능한 빈칸이 없는 경우 본인의 냄새 흔적이 남아있는 칸 우선순위 기준 탐색
                # 냄새가 남은 칸은 다른 상어가 오지 못하므로 상어번호 갱신 불필요
                if not is_move:
                    for i in range(4):
                        nx = x + dx[shark_priority[num][shark_direct[num] - 1][i] - 1]
                        ny = y + dy[shark_priority[num][shark_direct[num] - 1][i] - 1]
                        if 0 <= nx < N and 0 <= ny < N:
                            if shark_smell[nx][ny][0] == (num + 1):
                                area[x][y] = 0
                                area[nx][ny] = num + 1
                                visited[nx][ny] = True
                                shark_direct[num] = shark_priority[num][shark_direct[num] - 1][i]
                                break


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, k = map(int, input().split())

# 상어 위치가 담겨있는 배열
area = [list(map(int, input().split())) for _ in range(N)]
shark_smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
#초기 상어 위치에 냄새값 초기화
for i in range(N):
    for j in range(N):
        if area[i][j] > 0:
            shark_smell[i][j] = [area[i][j], k]
# 상어 초기 방향 설정(상, 하, 좌, 우)
shark_direct = list(map(int, input().split()))
# 상어 별 방향 우선순위(상, 하,좌, 우)
shark_priority = [[[], [], [],[]] for _ in range(M)]
for i in range(M):
    for j in range(4):
        shark_priority[i][j] = list(map(int, input().split()))

ans = 1
while True:
    # 상어 이동
    shark_move()
    smell_update()

    # 1번 상어만 남으면 중단
    only_one = True
    for i in range(N):
        for j in range(N):
            if area[i][j] > 1:
                only_one = False
    if only_one:
        break
    ans += 1
    if ans > 1000:
        ans = -1
        break
print(ans)