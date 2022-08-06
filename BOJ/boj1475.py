# 1475 방 번호

num_input = input()
num = []
for i in range(len(num_input)):
    num.append(int(num_input[i]))
cnt = 0

while num:
    # 6, 9 체크용 변수
    is_six = 2
    is_nine = 2
    for i in range(10):
        if i == 6:
            if 6 in num:
                if is_six:
                    num.remove(6)
                    is_six -= 1
                    is_nine -= 1 # 6, 9 을 동시에 카운트다운하여 0~9중 2번 발견 시 6, 9 탐색 종료
            if 9 in num:
                if is_nine:
                    num.remove(9)
                    is_six -= 1
                    is_nine -= 1
        elif i == 9:
            if 6 in num:
                if is_six:
                    num.remove(6)
                    is_six -= 1
                    is_nine -= 1
            if 9 in num:
                if is_nine:
                    num.remove(9)
                    is_six -= 1
                    is_nine -= 1
        elif i in num:
            num.remove(i)
    cnt += 1
print(cnt)