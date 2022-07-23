# 1244 스위치 켜고 끄기

N = int(input())
Lamp = list(map(int, input().split())) # 램프 스위치 리스트
std_No = int(input()) # 학생 수
Gen_and_No = [] #학생 성별, 배수 리스트

for _ in range(std_No):
    Gen_and_No.append(list(map(int, input().split()))) # 리스트에 학생정보 담는다

for i in range(len(Gen_and_No)):
    if Gen_and_No[i][0] == 1: # 남학생
        for j in range(N):
            if (j + 1) % Gen_and_No[i][1] == 0: # 배수 확인
                Lamp[j] = int(not Lamp[j])
    elif Gen_and_No[i][0] == 2: # 여학생
        Lamp[Gen_and_No[i][1] - 1] = int(not Lamp[Gen_and_No[i][1] - 1]) # 해당 번호부터 스위치 변경
        for j in range(N // 2): #좌 우 중 짧은 길이에 맞춰 대칭 여부 판단
            if Gen_and_No[i][1] + j > N or Gen_and_No[i][1] - j < 1: break
            if Lamp[Gen_and_No[i][1] - 1 + j] == Lamp[Gen_and_No[i][1] - 1 - j]: # 대칭 확인
                Lamp[Gen_and_No[i][1] - 1 + j] = int(not Lamp[Gen_and_No[i][1] - 1 + j])
                Lamp[Gen_and_No[i][1] - 1 - j] = int(not Lamp[Gen_and_No[i][1] - 1 - j])
            else:
                break

# 한 줄 마다 20개씩 출력
for i in range(N):
    if (i + 1) % 20 != 0:
        print(f'{Lamp[i]}', end=' ')
    else:
        print(f'{Lamp[i]}', end='\n')
