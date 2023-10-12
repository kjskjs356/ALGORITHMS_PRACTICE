import sys
sys.stdin = open('input.txt', 'r')

# 2022 삼성 하반기 오전 1번 싸움땅

n, m, k = map(int, input().split())
area = [[[] for _ in range(n)] for _ in range(n)]
ans = [0] * m
# area에 총 정보 저장
for i in range(n):
    gun = list(map(int, input().split()))
    for j in range(n):
        area[i][j].append(gun[j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

person = []
for _ in range(m):
    x, y, d, s = map(int, input().split())
    person.append([x - 1, y - 1, d, s, 0])

def LoserMove(idx, x, y):
    d = person[idx][2]
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 이동하려는 곳에 사람있거나 격자밖이면 시계방향 90도 회전 => d += 1
        if 0 <= nx < n and 0 <= ny < n:
            flag = True
            # 해당 칸에 사람이 존재하면 방향 바꾸기
            for idx2 in range(len(person)):
                # 자기자신은 패스
                if idx2 == idx: continue
                x2, y2 = person[idx2][0], person[idx2][1]
                if nx == x2 and ny == y2:
                    flag = False
                    break
            if not flag:
                d += 1
                if d >= 4: d %= 4
            else:
                # 이동 가능하면 대상의 좌표 및 방향 바꾸고 총 있는지 확인 후 교체하고 마무리
                person[idx][0], person[idx][1], person[idx][2] = nx, ny, d
                if area[nx][ny]:
                    bestGun = max(area[nx][ny])
                    bestGunIdx = area[nx][ny].index(bestGun)
                    person[idx][4] = bestGun
                    person[idx][2] = d
                    del area[nx][ny][bestGunIdx]
                return
        else:
            d += 1
            if d >= 4: d %= 4

def Fight(p1,p2, x, y):
    winner, loser = -1, -1
    # 첫번째 사람의 전투력
    power1 = person[p1][3] + person[p1][4]
    # 두번째 사람의 전투력
    power2 = person[p2][3] + person[p2][4]
    if power1 > power2:
        winner, loser = p1, p2
    elif power2 > power1:
        winner, loser = p2, p1
    else:
        # 총 파워가 동일하면 초기 능력치가 높은 쪽이 승리
        if person[p1][3] > person[p2][3]:
            winner, loser = p1, p2
        else:
            winner, loser = p2, p1
    ans[winner] += abs(power1 - power2)
    # 패자 먼저 총을 떨어뜨리고 이동
    myGun = person[loser][4]
    area[x][y].append(myGun)
    person[loser][4] = 0
    LoserMove(loser, x, y)
    # 승자는 제일 좋은 총으로 교체
    myGun2 = person[winner][4]
    bestGun = max(area[x][y])
    bestGunIdx = area[x][y].index(bestGun)
    if myGun2 < bestGun:
        person[winner][4] = bestGun
        del area[x][y][bestGunIdx]
        if myGun2 > 0: area[x][y].append(myGun2)


def Move(idx):
    x, y, d, s, myGun = person[idx]
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 격자내에서 이동하는 경우 for문 탈출
        if 0 <= nx < n and 0 <= ny < n:
            # 해당 칸에 사람이 존재하는지 먼저 체크하고 있으면 결투
            for idx2 in range(len(person)):
                # 자기자신은 패스
                if idx2 == idx: continue
                x2, y2 = person[idx2][0], person[idx2][1]
                if nx == x2 and ny == y2:
                    person[idx][0], person[idx][1], person[idx][2] = nx, ny, d
                    Fight(idx, idx2, nx, ny)
                    return
            # 사람이 없으면 해당 칸에 총이 있으면 줍거나 교체
            if area[nx][ny]:
                # 가장 좋은 총 바로 줍기
                bestGun = max(area[nx][ny])
                bestGunIdx = area[nx][ny].index(bestGun)
                if myGun < bestGun:
                    person[idx][4] = bestGun
                    del area[nx][ny][bestGunIdx]
                    if myGun > 0: area[nx][ny].append(myGun)
            person[idx][0], person[idx][1], person[idx][2] = nx, ny, d
            return
        else:
            d += 2
            if d >= 4: d %= 4
            person[0]

for _ in range(k):
    # 앞사람부터 순서대로 진행
    for num in range(m):
        Move(num)
print(' '.join(map(str, ans)))
