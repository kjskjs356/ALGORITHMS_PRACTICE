def solution(tasks):
    answer = 0
    check = []
    if len(tasks) == 1:
        return -1
    for i in range(len(tasks) - 1):
        if tasks[i] in check:
            continue
        else:
            check.append(tasks[i])
        cnt = 1
        for j in range(i + 1, len(tasks)):
            if tasks[i] == tasks[j]:
                cnt += 1
        if cnt % 3 == 0:
            answer += 1
        elif cnt % 2 == 0:
            answer += 1
        else:
            return -1
            
    return answer

print(solution([1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5]))