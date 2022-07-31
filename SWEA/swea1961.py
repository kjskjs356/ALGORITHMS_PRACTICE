# 1961 숫자배열 회전

T = int(input()) # 테스트케이스
for n in range(T):
    N = int(input()) # 사각형 크기 NxN
    rect = []
    rect_90 = []
    rect_180 = []
    rect_270 =[]
    for _ in range(N):
        rect.append(list(map(int, input().split()))) #한 줄에 N개 숫자 N줄 반복

    for i in range(N): # 90도 회전
        tmp = []
        for j in range(N):
            tmp.append(rect[N - 1 - j][i])
        rect_90.append(tmp)

    for i in range(N): # 180도 회전
        tmp = []
        for j in range(N):
            tmp.append(rect_90[N - 1 - j][i])
        rect_180.append(tmp)
    
    for i in range(N): # 270도 회전
        tmp = []
        for j in range(N):
            tmp.append(rect_180[N - 1 - j][i])
        rect_270.append(tmp)
    1
    print(f'#{n+1}')
    for i in range(N):
        for j in range(N):
            print(rect_90[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(rect_180[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(rect_270[i][j], end='')
        print('')