T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    h = list(map(int, input().split()))
    # 지형 개수 1이면 정답 1 출력
    if N == 1:
        top = 1
    else:
        top = 0
        is_up = False
        # 처음부터 탐색하여 봉우리 여부 체크
        for i in range(N):
            # 맨앞 지형은 다음지형보다 높으면 봉우리인정
            if i == 0:
                is_up = True
            # 맨뒤 지형은 이전지형보다 높으면 봉우리 인정
            elif i == N - 1:
                if h[i] > h[i - 1]:
                    top += 1
                elif is_up:
                    top += 1
            else:
                # 중간 지형
                if h[i] > h[i - 1]:
                    is_up = True
                # 동일 높이 봉우리는 패스
                if h[i] == h[i - 1]:
                    continue
                # 다음 봉우리값이 더 작을 경우 is_up 여부에 따라 봉우리로 인정 여부 확인
                if h[i] < h[i - 1]:
                    if is_up:
                        top += 1
                        is_up = False
    print('#{} {}' .format(tc, top))
