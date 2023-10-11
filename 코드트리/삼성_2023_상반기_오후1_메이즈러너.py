import sys
sys.stdin = open('input.txt', 'r')

# 2023 삼성 상반기 오후 1번 메이즈러너

N, M, K = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
personArea = [[0] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    personArea[x - 1][y - 1] += 1
x, y = map(int, input().split())
rx, ry = x - 1, y - 1
area[x - 1][y - 1] = -1
ans = 0

# 한명이상의 참가자와 츨구 포함 가장 작은 정사각형 선택
# 크기가 같은게 2개이상이면 좌상단 좌표 기준 x좌표 1순위, y좌표 2순위
# 시계방향 90도 회전 후 회전된 벽 내구도 -1

# 최소사각형 만들 참가자 좌표 선택
def selectLocation(ex, ey):
    minLen = 99
    targetX, targetY = -1, -1
    for i in range(len(person)):
        if person[i][0] == -1: continue
        sx, sy = person[i][0], person[i][1]
        tempMin = max(abs(ex - sx), abs(ey - sy))
        # 최단거리일 경우 갱신
        if minLen > tempMin:
            minLen = tempMin
            targetX, targetY = sx, sy
        # 거리가 같을 경우 더 위쪽 & 더 왼쪽 사람이 우선순위
        elif minLen == tempMin:
            if sx < targetX:
                minLen = tempMin
                targetX, targetY = sx, sy
            elif sx == targetX:
                if sy <= targetY:
                    minLen = tempMin
                    targetX, targetY = sx, sy
    return minLen

# 사각형 영역 선택 후 회전하기

def makeRect(num):
    tx, ty = -1, -1
    breaker = False
    for i in range(N - num):
        if breaker:
            break
        for j in range(N - num):
            isPerson = False
            isExit = False
            # 전체영역에서 참가자 최소1명과 탈출구를 모두 포함하는 좌상단 사각형 찾기
            for k in range(i, i + num + 1):
                for l in range(j, j + num + 1):
                    if area[k][l] == -1: isExit = True
                    if personArea[k][l] > 0: isPerson = True
            if isPerson and isExit:
                tx, ty = i, j
                breaker = True
                break

    m = num + 1
    # 영역 회전
    tempArr = [[0] * m for _ in range(m)]
    tempArr2 = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            tempArr[i][j] = area[tx + i][ty + j]
            tempArr2[i][j] = personArea[tx + i][ty + j]

    rotateArr = list(map(list, zip(*tempArr[::-1])))
    rotateArr2 = list(map(list, zip(*tempArr2[::-1])))

    # 맵 갱신
    for i in range(m):
        for j in range(m):
            area[tx + i][ty + j] = rotateArr[i][j]
            personArea[tx + i][ty + j] = rotateArr2[i][j]
            if area[tx + i][ty + j] > 0: area[tx + i][ty + j] -= 1

for num in range(K):
    # 모든 참가자가 최단거리로 이동가능여부 확인 후 이동(상하 방향 우선)
    # 참가자 있는곳 좌표를 배열에 저장
    person = []
    for i in range(N):
        for j in range(N):
            if personArea[i][j] > 0:
                person.append([i, j, personArea[i][j]])

    # 최초 사람 위치
    for i in range(len(person)):
        #sx, xy : 참가자의 현재좌표 / rx, ry : 툴구 좌표, cnt : 인원수
        sx, sy, cnt = person[i][0], person[i][1], person[i][2]
        # 초기값이 탈출구인 참가자는 즉시 탈출
        if sx == rx and sy == ry:
            person[i][0], person[i][1] = -1, -1
            continue
        # 탈출구, 참가자 x축 동일
        if sx == rx:
            # 탈출구가 더 오른쪽
            if ry > sy:
                # 참가자가 탈출구 방향으로 진행 가능한지 확인
                if area[sx][sy + 1] <= 0:
                    ans += cnt
                    personArea[sx][sy + 1] += cnt
                    personArea[sx][sy] -= cnt
                    sy += 1
            # 탈출구가 더 왼쪽
            else:
                if area[sx][sy - 1] <= 0:
                    ans += cnt
                    personArea[sx][sy - 1] += cnt
                    personArea[sx][sy] -= cnt
                    sy -= 1
        # 탈출구, 참가자 y축 동일
        elif sy == ry:
            # 탈출구가 더 위쪽
            if rx < sx:
                # 참가자가 탈출구 방향으로 진행 가능한지 확인
                if area[sx - 1][sy] <= 0:
                    ans += cnt
                    personArea[sx - 1][sy] += cnt
                    personArea[sx][sy] -= cnt
                    sx -= 1
            # 탈출구가 더 아래쪽
            else:
                if area[sx + 1][sy] <= 0:
                    ans += cnt
                    personArea[sx + 1][sy] += cnt
                    personArea[sx][sy] -= cnt
                    sx += 1
        # 참가자가 탈출구의 좌상 위치
        elif sx < rx and sy < ry:
            if area[sx + 1][sy] <= 0:
                ans += cnt
                personArea[sx + 1][sy] += cnt
                personArea[sx][sy] -= cnt
                sx += 1
            elif area[sx][sy + 1] <= 0:
                ans += cnt
                personArea[sx][sy + 1] += cnt
                personArea[sx][sy] -= cnt
                sy += 1
        # 참가자가 탈출구의 좌하 위치
        elif sx > rx and sy < ry:
            if area[sx - 1][sy] <= 0:
                ans += cnt
                personArea[sx - 1][sy] += cnt
                personArea[sx][sy] -= cnt
                sx -= 1
            elif area[sx][sy + 1] <= 0:
                ans += cnt
                personArea[sx][sy + 1] += cnt
                personArea[sx][sy] -= cnt
                sy += 1
        # 참가자가 탈출구의 우상 위치
        elif sx < rx and sy > ry:
            if area[sx + 1][sy] <= 0:
                ans += cnt
                personArea[sx + 1][sy] += cnt
                personArea[sx][sy] -= cnt
                sx += 1
            elif area[sx][sy - 1] <= 0:
                ans += cnt
                personArea[sx][sy - 1] += cnt
                personArea[sx][sy] -= cnt
                sy -= 1
        # 참가자가 탈출구의 우하 위치
        elif sx > rx and sy > ry:
            if area[sx - 1][sy] <= 0:
                ans += cnt
                personArea[sx - 1][sy] += cnt
                personArea[sx][sy] -= cnt
                sx -= 1
            elif area[sx][sy - 1] <= 0:
                ans += cnt
                personArea[sx][sy - 1] += cnt
                personArea[sx][sy] -= cnt
                sy -= 1
        person[i][0], person[i][1] = sx, sy
        # 참가자가 탈출했는지 체크
        if person[i][0] == rx and person[i][1] == ry:
            personArea[rx][ry] = 0

    # 사람 배열 갱신
    person = []
    for i in range(N):
        for j in range(N):
            if personArea[i][j] > 0:
                person.append([i, j, personArea[i][j]])

    maxPerson = max(map(max, personArea))
    # 모두 탈출했으면 종료
    if maxPerson == 0: break
    # 모든 참가자가 이동마치면 가장 작은 정사각형 구하기
    minLen = selectLocation(rx, ry)
    makeRect(minLen)
    # 출구 좌표 갱신
    for i in range(N):
        for j in range(N):
            if area[i][j] == -1:
                rx, ry = i, j
                break

print(ans)
print(rx + 1, ry + 1)