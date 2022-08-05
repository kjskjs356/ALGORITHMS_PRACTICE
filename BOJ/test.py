def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    cnt = 0
    num = 0
    while cnt != len(requests):
        if not sticky:
            answer[num].append(requests[cnt])
            num += 1
            cnt += 1
            if num == len(answer):
                num = 0
        else:
            if cnt == 0:
                answer[num].append(requests[cnt])
                cnt += 1
                continue

            if requests[cnt] == requests[cnt - 1]:
                answer[num].append(requests[cnt])
                cnt += 1

            else:
                if num == len(answer) - 1:
                    num = 0
                else:
                    num += 1
                answer[num].append(requests[cnt])
                cnt += 1
    while [] in answer:
        answer.remove([])
    return answer

servers = 4
sticky = True
requests = [1]

print(solution(servers, sticky, requests))