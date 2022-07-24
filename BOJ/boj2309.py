# 2309 일곱 난쟁이

dwarf= [int(input()) for _ in range(0,9)]
dwarf.sort()
dwarf_no = [0, 0, 1, 1, 1, 1, 1, 1, 1]
result = [x*y for x, y in zip(dwarf, dwarf_no)]
breaker = False

# 처음 배열부터 합 확인
if sum(result) == 100:
    for i in range(len(result)):
            if result[i] != 0:
                print(result[i])

# 한 요소씩 돌아가며 합 확인
else:
    for i in range(len(dwarf)):
        if breaker == True:
            break
        for j in range(i + 1, len(dwarf)):
            if breaker == True:
                break
            dwarf_no = [1] * 9
            dwarf_no[i] = dwarf_no[j] = 0
            result = [x*y for x, y in zip(dwarf, dwarf_no)]
            if sum(result) == 100:
                for i in range(len(result)):
                    if result[i] != 0:
                        print(result[i])
                        breaker = True
        