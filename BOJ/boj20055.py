#20055 컨베이어 벨트 위의 로봇

from collections import deque

N, K = map(int, input().split())
# 벨트 길이 = 2N
belt = deque(list(map(int, input().split())))
robot = deque([False] * N)
step = 0
while belt.count(0) < K:
    #1순위로 회전 시행
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    #마지막 로봇부터 체크
    if robot[-1]:
        robot[-1] = False
    for i in range(N - 2, -1, -1):
        # 로봇이 있는 경우에 작업 시행
        if robot[i]:
            if not robot[i + 1] and belt[i + 1] > 0:
                robot[i + 1] = True
                belt[i + 1] -= 1
                robot[i] = False
                if robot[-1]:
                    robot[-1] = False
    # 첫 위치에 로봇 올릴수 있는 체크
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
    step += 1
print(step)