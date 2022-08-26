# 6359 만취한 상범

T = int(input())
for _ in range(T):
    n = int(input())
    # 0: 잠김, 1: 열림
    room = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j > n:
                break
            if room[i * j] == 0:
                room[i * j] = 1
            else:
                room[i * j] = 0
    print(room.count(1))