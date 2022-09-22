# 20056 마법사 상어와 파이어볼


def direct(arr):
    # 모두 홀수 or 짝수: 리턴1, 그외 : 리턴 0
    is_odd, is_even = False, False
    for x in arr:
        if x % 2 == 0:
            is_even = True
        elif x % 2 == 1:
            is_odd = True
    if is_odd and is_even:
        return 0
    else:
        return 1


# 0, 1, 2, 3, 4, 5, 6, 7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
field = [[0] * N for _ in range(N)]
# 파이어볼 => 0:행, 1:열, 2:질량, 3:속도, 4:방향
fire = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fire.append([r, c, m, s, d])
result = 0

while K > 0:
    print('step {}'.format(K))
    # 파이어볼 이동
    for i in range(len(fire)):
        fire[i][0] += dx[fire[i][4]] * fire[i][3]
        fire[i][1] += dy[fire[i][4]] * fire[i][3]
        fire[i][0] %= N
        fire[i][1] %= N
        field[fire[i][0] % N][fire[i][1] % N] += 1
    for i in range(len(fire)):
        print(fire[i])
    print()
    for i in range(N):
        for j in range(N):
            field[i][j] = 0
            for k in range(len(fire)):
                if fire[k][0] == i and fire[k][1] == j:
                    field[i][j] += 1
    for i in range(N):
        print(field[i])
    print()
    # 겹친 파이어볼 조사(겹치는게 없을 때까지)
    for i in range(N):
        for j in range(N):
            if field[i][j] >= 2:
                flag = True
                sum_mass, sum_speed = 0, 0
                sum_direct = []
                # 겹친 파이어볼의 질량, 속도, 방향 체크
                for k in range(len(fire)):
                    if fire[k][0] == i and fire[k][1] == j:
                        sum_mass += fire[k][2]
                        sum_speed += fire[k][3]
                        sum_direct.append(fire[k][4])
                new_mass = sum_mass // 5
                new_speed = sum_speed // field[i][j]
                # 질량이 0이면 소멸
                if new_mass == 0:
                    flag = False
                # 남아있으면 4방향으로 분산
                if flag:
                    # 방향이 모두 홀수이거나 짝수인 경우
                    if direct(sum_direct) == 1:
                        for k in range(4):
                            fire.append([i, j, new_mass, new_speed, k * 2])
                            # field[i + dx[k * 2]][j + dy[k * 2]] += 1
                    # 그 외
                    elif direct(sum_direct) == 0:
                        for k in range(4):
                            fire.append([i, j, new_mass, new_speed, k * 2 + 1])
                            # field[i + dx[k * 2 + 1]][j + dy[k * 2 + 1]] += 1
                # 중심에 있는 파이어볼은 좌표를 찾아서 제거
                fire = [x for x in fire if x[0] != i or x[1] != j or x[2] == new_mass]
                field[i][j] = 0
                for k in range(len(fire)):
                    print(fire[k])
                print()
    K -= 1

for i in range(len(fire)):
    result += fire[i][2]
print(result)