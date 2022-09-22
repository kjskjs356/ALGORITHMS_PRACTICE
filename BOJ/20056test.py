# 20056 마법사 상어와 파이어볼

from collections import deque


# 0, 1, 2, 3, 4, 5, 6, 7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
field = [[[]for _ in range(N)] for _ in range(N)]
# 파이어볼 => 0:행, 1:열, 2:질량, 3:속도, 4:방향
fire = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    field[r][c].append([m, s, d])
result = 0
for _ in range(K):
    # 파이어볼 이동
    new_field = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while field[i][j]:
                ni, nj = i, j
                m, s, d = field[i][j].pop(0)
                ni = (ni + dx[d] * s) % N
                nj = (nj + dy[d] * s) % N
                new_field[ni][nj].append((m, s, d))
    for i in range(N):
        for j in range(N):
            field[i][j].append(new_field[i][j])
    for i in range(N):
        print(field[i])


    # 겹친 파이어볼 조사(겹치는게 없을 때까지)
    for i in range(N):
        for j in range(N):
            if field[i][j] >= 2:
                sum_mass, sum_speed = 0, 0
                # 겹친 파이어볼의 질량, 속도, 방향 체크
                remove_list = deque()
                is_odd, is_even = False, False
                for k in range(len(fire)):
                    if fire[k][0] == i and fire[k][1] == j:
                        sum_mass += fire[k][2]
                        sum_speed += fire[k][3]
                        if fire[k][4] % 2 == 0:
                            is_even = True
                        else:
                            is_odd = True
                        remove_list.append(fire[k])
                for rem in remove_list:
                    fire.remove(rem)
                new_mass = sum_mass // 5
                new_speed = sum_speed // field[i][j]
                # 질량이 0이면 소멸
                if new_mass == 0:
                    continue
                # 남아있으면 4방향으로 분산
                else:
                    # 방향이 홀짝 섞여 있을 경우
                    if is_even and is_odd:
                        fire.append([i, j, new_mass, new_speed, 1])
                        fire.append([i, j, new_mass, new_speed, 3])
                        fire.append([i, j, new_mass, new_speed, 5])
                        fire.append([i, j, new_mass, new_speed, 7])
                    # 그 외
                    else:
                        fire.append([i, j, new_mass, new_speed, 0])
                        fire.append([i, j, new_mass, new_speed, 2])
                        fire.append([i, j, new_mass, new_speed, 4])
                        fire.append([i, j, new_mass, new_speed, 6])
                field[i][j] = 0

for i in range(len(fire)):
    result += fire[i][2]
print(result)