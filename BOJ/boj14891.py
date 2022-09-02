# 14891 톱니바퀴

from collections import deque

def cogwheel_rotate(arr, d):
    # d: 1일 경우, 시계방향, -1일 경우 반시계방향
    if d == 1:
        arr.appendleft(arr.pop())
    elif d == -1:
        arr.append(arr.popleft())

def check_wheel(idx, cogwheel, d):
    print(idx)
    # 제일 왼쪽 톱니바퀴
    if idx == 0:
        if cogwheel[idx][2] != cogwheel[idx + 1][6]:
            check_wheel(idx + 1, cogwheel, -d)
        cogwheel_rotate(cogwheel[idx], d)
    # 제일 오른쪽 톱니바퀴
    elif idx == 3:
        if cogwheel[idx][6] != cogwheel[idx - 1][2]:
            check_wheel(idx - 1, cogwheel, -d)
        cogwheel_rotate(cogwheel[idx], d)
    elif 1 <= idx <= 2:
        # 오른쪽 체크
        if cogwheel[idx][2] != cogwheel[idx + 1][6]:
            check_wheel(idx + 1, cogwheel, -d)
        # 왼쪽 체크
        if cogwheel[idx][6] != cogwheel[idx - 1][2]:
            check_wheel(idx - 1, cogwheel, -d)
        cogwheel_rotate(cogwheel[idx], d)
    else:
        return

# 톱니 정보 (인덱스 2, 6 맞물림 이용)
cogwheel = []
for _ in range(4):
    cogwheel.append(deque(list(map(int, input()))))
# 회전 수
K = int(input())
#회전 정보
rotation = []
for _ in range(K):
    rotation.append(list(map(int, input().split())))
result = 0
# K만큼 톱니 회전
for i in range(0, K):
    choice, direct = rotation[i][0] - 1, rotation[i][1]
    check_wheel(choice, cogwheel, direct)
    for i in range(4):
        print(cogwheel[i])
    print()
#점수 체크
for i in range(4):
    result += cogwheel[i][0] * 2**i
print(result)