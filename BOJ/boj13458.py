    # 13458 시험감독

    N = int(input())
    student = list(map(int, input().split()))
    # 값이 큰 응시자부터 빼기 위해 내림차순 정리
    B, C = map(int, input().split())
    result = 0
    # 총감독관 먼저 투입
    for i in range(N):
        student[i] -= B
        if student[i] < 0:
            student[i] = 0
        result += 1

    while sum(student) > 0:
        for i in range(N):
            result += student[i] // C
            student[i] %= C
            if student[i] > 0:
                result += 1
                student[i] = 0
    print(result)