import sys
sys.stdin = open('input.txt', 'r')

# 2021 삼성 하반기 오후 2번 미로타워디펜스

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
attack = []
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dx2 = [0, 1, 0, -1]
dy2 = [-1, 0, 1 ,0]

for _ in range(m):
    d, p = map(int, input().split())
    attack.append([d, p])

def AttackMonster(d, p):
    temp = 0
    x, y = n // 2, n // 2
    for k in range(1, p + 1):
        nx = x + dx[d] * k
        ny = y + dy[d] * k
        if area[nx][ny] > 0:
            temp += area[nx][ny]
            area[nx][ny] = 0
    return temp

def Supplement():
    # 중앙부터 바깥까지 큐에 집어넣기
    # cnt: 기준 이동칸
    # line: 이동중인 길이, 0이되면 cnt값으로 초기화
    # turn: 2번 회전할때마다(0이 될때마다) cnt 1씩 추가
    x, y = n // 2, n // 2
    cnt, line, turn, d = 1, 1, 2, 0
    # 0,0 도달할때까지 반복
    while True:
        nx = x + dx2[d]
        ny = y + dy2[d]
        if area[nx][ny] > 0:
            q.append(area[nx][ny])
        if nx == 0 and ny == 0: return
        line -= 1
        if line == 0:
            d += 1
            if d == 4: d %= 4
            turn -= 1
            if turn == 0:
                cnt += 1
                # 가장 외곽인 경우
                if cnt == n - 1:
                    turn = 3
                else:
                    turn = 2
            line = cnt
        x, y = nx, ny

def Remove(q):
    global ans
    # 배열의 끝에 다다를떄까지 반복
    while True:
        first, idx, num, cnt = 0, 0, q[0], 1
        flag = True
        while True:
            idx += 1
            # 마지막에 다다랐을 시
            if idx == len(q) - 1:
                # 같을 숫자 4연속이면 누적 후 제거
                if q[idx] == num and cnt >= 3:
                    cnt += 1
                    ans += num * cnt
                    q = q[:first]
                elif q[idx] != num and cnt >= 4:
                    ans += num * cnt
                    q = q[:first] + q[idx:]
                break
            # 같은 숫자 연속이면 누적
            if q[idx] == num:
                cnt += 1
            # 다른 숫자가 나올 시 이전숫자가 연속 4번이상인지 확인, 4번이상이면 해당 인덱스 부터 삭제
            else:
                if cnt >= 4:
                    ans += num * cnt
                    num = q[idx]
                    cnt = 1
                    q = q[:first] + q[idx:]
                    idx = first
                    flag = False
                else:
                    num = q[idx]
                    cnt = 1
                    first = idx
        if flag: return q

def Match(q):
    q2 = []
    idx, num, cnt = 1, q[0], 1
    while True:
        # 끝에 다다랐을때와 다다르지 않았을때 구분
        if idx == len(q) - 1:
            # 끝 숫자가 이전과 동일하면 카운팅 후 계산
            if q[idx] == num:
                q2.append(cnt + 1)
                q2.append(num)
            # 다르면 별도로 계산
            else:
                q2.append(cnt)
                q2.append(num)
                q2.append(1)
                q2.append(q[idx])
            return q2
        else:
            # 같은 숫자면 누적
            if q[idx] == num:
                cnt += 1
            # 다른 숫자면 계산
            else:
                q2.append(cnt)
                q2.append(num)
                # 현재 숫자, 카운트 갱신
                num = q[idx]
                cnt = 1
        idx += 1

def ReArrange(q):
    area2 = [[0] * n for _ in range(n)]
    # 중앙부터 바깥까지 큐에 집어넣기
    # cnt: 기준 이동칸
    # line: 이동중인 길이, 0이되면 cnt값으로 초기화
    # turn: 2번 회전할때마다(0이 될때마다) cnt 1씩 추가
    x, y = n // 2, n // 2
    cnt, line, turn, d, idx = 1, 1, 2, 0, 0
    # 0,0 도달할때까지 반복
    while True:
        nx = x + dx2[d]
        ny = y + dy2[d]
        area2[nx][ny] = q[idx]
        line -= 1
        if line == 0:
            d += 1
            if d == 4: d %= 4
            turn -= 1
            if turn == 0:
                # 가장 외곽인 경우
                cnt += 1
                if cnt == n - 1: turn = 3
                else: turn = 2
            line = cnt
        idx += 1
        if nx == 0 and ny == 0: return area2
        if idx == len(q): return area2
        x, y = nx, ny

for k in range(m):
    # 1. 턴마다 d 방향으로 p칸만큼 공격, 제거된 몬스터 점수계산
    [d, p] = attack[k]
    ans += AttackMonster(d, p)
    # 2. 빈공간 메꾸기(배열을 이용하여 1차원적 해석)
    q = []
    Supplement()
    # 3. 더이상 삭제가능한 몬스터 없을때까지 삭제, 삭제된 몬스터 점수 계산
    q = Remove(q)
    # 4. 몬스터 재배치 : 각 숫자의 개수를 계산해서 [총 개수, 숫자의크기]
    # 배열을 초과한다면 초과부분은 무시하기(중요)
    q = Match(q)
    area = ReArrange(q)
print(ans)