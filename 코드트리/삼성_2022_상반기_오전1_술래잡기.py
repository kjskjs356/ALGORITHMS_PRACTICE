import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 상반기 오전 1번 술래잡기

# n: 맵크기, m: 도망자 수, h: 나무 수, k: 총 턴의 수
n, m, h, k = map(int, input().split())
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dx2 = [-1, 0, 1, 0]
dy2 = [0, 1, 0, -1]

# 나무 지도
tree = [[0] * n for _ in range(n)]
# 도망자 지도
person = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, d = map(int, input().split())
    if d == 1:
        person[x - 1][y - 1].append(0)
    else:
        person[x - 1][y - 1].append(1)

for _ in range(h):
    x, y = map(int, input().split())
    tree[x - 1][y - 1] = 1

observer = [n // 2, n // 2]
# 술래 관련 변수 - num: 최대 직진 횟수 cnt: 방향전환 여부 체크용 변수, turn: 턴 하기 전 직진수
num = 1
cnt = 2
turn = 1
direct = 0
reverse = False

def ObserverMove(t):
    global num, cnt, turn, direct, reverse, observer
    x, y = observer[0], observer[1]
    nx = x + dx2[direct % 4]
    ny = y + dy2[direct % 4]
    # 끝 또는 정중앙에 도착한 경우 방향
    if nx == 0 and ny == 0 or nx == n // 2 and ny == n // 2:
        direct += 2
        reverse = not reverse
        if reverse == True: cnt = 3
        elif reverse == False: cnt = 2
        turn = num
    # 이동방향, 바라보는 방향 체크
    else:
        # 중앙에서 바깥으로 이동하는 경우
        if reverse == False:
            # turn -> 0 될때까지 해당방향 직진, 0이 되면 cnt 1씩 감소, 시계방향으로 방향 전환
            turn -= 1
            if turn == 0:
                direct += 1
                cnt -= 1
                # cnt 0이 되면 카운트 리셋, 최대 이동거리 1 증가
                if cnt == 0:
                    num += 1
                    turn = num
                    if turn == n - 1: cnt = 3
                    else : cnt = 2
                else:
                    turn = num
        # 바깥에서 중앙으로 이동하는 경우
        if reverse == True:
            # turn -> 0 될때까지 해당방향 직진, 0이 되면 cnt 1씩 감소, 시계방향으로 방향 전환
            turn -= 1
            if turn == 0:
                direct -= 1
                cnt -= 1
                # cnt 0이 되면 2로 리셋, 최대 이동거리 1 증가
                if cnt == 0:
                    num -= 1
                    turn = num
                    if turn == n - 1: cnt = 3
                    else : cnt = 2
                else:
                    turn = num
    # 이동한 칸으로 갱신
    x, y = nx, ny
    observer = [x, y]
    # 해당위치에서 바라보는 방향 기준 자신의 칸 포함 3칸이내로 도망자 있는지 체크
    personCnt= 0
    for i in range(3):
        nx = x + dx2[direct % 4] * i
        ny = y + dy2[direct % 4] * i
        if 0 <= nx < n and 0 <= ny < n:
            # 나무가 있으면 패스
            if tree[nx][ny] > 0: continue
            if person[nx][ny]:
                personCnt += len(person[nx][ny])
                person[nx][ny] = []
        else:
            break
    return t * personCnt

def PersonMove():
    person2 = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 해당 칸에 사람 존재하면 술래와 3칸 이내의 경우 이동시키기
            if person[i][j] and abs(observer[0] - i) + abs(observer[1] - j) <= 3:
                for d in person[i][j]:
                    x, y = i, j
                    nx = x + dx[d % 4]
                    ny = y + dy[d % 4]
                    # 격자 안벗어남
                    if 0 <= nx < n and 0 <= ny < n:
                        # 이동하려는 칸에 술래 있으면 현 위치 유지
                        if nx == observer[0] and ny == observer[1]:
                            person2[x][y].append(d)
                        else: person2[nx][ny].append(d)
                    # 격자 벗어나면 방향반대로 바꾸기
                    elif nx < 0 or nx >= n:
                        d += 2
                        if d >= 4: d %= 4
                        nx = x + dx[d % 4]
                        ny = y + dy[d % 4]
                        # 이동하려는 칸에 술래 있으면 현 위치 유지
                        if nx == observer[0] and ny == observer[1]:
                            person2[x][y].append(d)
                        else: person2[nx][ny].append(d)
                    elif ny < 0 or ny >= n:
                        d += 2
                        if d >= 4: d %= 4
                        nx = x + dx[d % 4]
                        ny = y + dy[d % 4]
                        # 이동하려는 칸에 술래 있으면 현 위치 유지
                        if nx == observer[0] and ny == observer[1]:
                            person2[x][y].append(d)
                        else: person2[nx][ny].append(d)
                # 칸 갱신을 위해 현재 칸 리셋
                person[i][j] = []
            else:
                for p in person[i][j]:
                    person2[i][j].append(p)
    # 도망자 새로운 위치로 갱신
    for i in range(n):
        for j in range(n):
            if person2[i][j]:
                person[i][j] = person2[i][j]

for t in range(1, k + 1):
    # 도망자 이동
    PersonMove()
    # 술래 이동
    temp = ObserverMove(t)
    ans += temp
print(ans)
