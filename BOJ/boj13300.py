# 방 배정

N, K = map(int, input().split())
student = []
for _ in range(N):
    student.append(list(map(int, input().split())))
# 성별 오름차순 => 학년 오름차순
student.sort(key=lambda x:(x[0], x[1]))
room = 1
cnt = 1
for i in range(1, N):
    if student[i][0] == student[i - 1][0] and student[i][1] == student[i - 1][1]:
        if cnt == K:
            room += 1
            cnt = 1
        else:
            cnt += 1
    else:
        room += 1
        cnt = 1
print(room)