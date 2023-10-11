import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 상반기 오전 2번 예술성

from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 조합 함수
def Comb(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for j in Comb(arr[1 + i:], n - 1):
                yield [arr[i]] + j

# target : 같은 그룹에 속한 숫자인지, num : 해당 그룹 번호
def SetGroup(a, b, target, num):
    q = deque()
    q.append((a, b))
    group[a][b] = num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] == target and group[nx][ny] == 0:
                    group[nx][ny] = num
                    cnt += 1
                    q.append((nx, ny))
    return cnt

def Search(a, b, start, end):
    q = deque()
    q.append((a, b))
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        if group[x][y] == end:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if group[nx][ny] == start or group[nx][ny] == end:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

# 두 그룹의 조화로움 비교
def Check(g1, g2):
    check = False
    breaker = False
    for i in range(n):
        if breaker: break
        for j in range(n):
            if group[i][j] == g1:
                check = Search(i, j, g1, g2)
                breaker = True
                break
            elif group[i][j] == g2:
                check = Search(i, j, g2, g1)
                breaker = True
                break
    return check


def WallCheck(a, b, s, e):
    q = deque()
    q.append((a, b))
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if group[nx][ny] == s:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif group[nx][ny] == e:
                    cnt += 1
    return cnt

# 조화로움 계산
def Art(g1, g2):
    temp = (g1[2] + g2[2]) * g1[1] * g2[1]
    # 맞닿아 있는 변의 수 계산
    for i in range(n):
        for j in range(n):
            if group[i][j] == g1[0]:
                cnt = WallCheck(i, j, g1[0], g2[0])
            elif group[i][j] == g2[0]:
                cnt = WallCheck(i, j, g2[0], g1[0])
    temp *= cnt
    return temp

def Rotate():
    cross = [arr[:] for arr in area]
    cross = list(map(list, zip(*cross)))[::-1]
    square1 = [arr[:n // 2] for arr in area[:n // 2]]
    square1 = list(map(list, zip(*square1[::-1])))
    square2 = [arr[n // 2 + 1:] for arr in area[:n // 2]]
    square2 = list(map(list, zip(*square2[::-1])))
    square3 = [arr[:n // 2] for arr in area[n // 2 + 1:]]
    square3 = list(map(list, zip(*square3[::-1])))
    square4 = [arr[n // 2 + 1:] for arr in area[n // 2 + 1:]]
    square4 = list(map(list, zip(*square4[::-1])))

    for i in range(n):
        for j in range(n):
            if i <= n // 2 - 1 and j <= n // 2 - 1:
                area[i][j] = square1[i][j]
            elif i <= n // 2 - 1 and n // 2 + 1 <= j:
                area[i][j] = square2[i][j - (n // 2 + 1)]
            elif n // 2 + 1 <= i and j <= n // 2 - 1:
                area[i][j] = square3[i - (n // 2 + 1)][j]
            elif n // 2 + 1 <= i and n // 2 + 1 <= j:
                area[i][j] = square4[i - (n // 2 + 1)][j - (n // 2 + 1)]
            elif i == n // 2 or j == n // 2:
                area[i][j] = cross[i][j]

# 초기, 1회전, 2회전, 3회전 이후의 예술점수 합산 출력

for _ in range(4):
    # 그룹 구분하기
    groupNum = []
    group = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            if group[i][j] == 0:
                cnt = SetGroup(i, j, area[i][j], num)
                groupNum.append([num, area[i][j], cnt])
                num += 1

    # 그룹 2개씩 선택해서 조화로움 확인(인덱스 구분 - 0: 그룹번호, 1: 그룹 숫자, 2: 칸 개수)
    for g1, g2 in Comb(groupNum, 2):
        if not Check(g1[0], g2[0]): continue
        ans += Art(g1, g2)
    # 회전 실행
    Rotate()
print(ans)
