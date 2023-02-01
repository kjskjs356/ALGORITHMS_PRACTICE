def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_day = map(int, today.split("."))
    total_time = t_year * 86400 * 28 * 12 + t_month * 86400 * 28 + t_day * 86400
    terms_list = dict()
    # 약관 객체로 구분
    for term in terms:
        term_name, term_date = map(str, term.split(' '))
        terms_list[term_name] = int(term_date)

    for i in range(len(privacies)):
        p_date, p_term = map(str, privacies[i].split(" "))
        p_year, p_month, p_day = map(int, p_date.split('.'))
        p_time = p_year * 86400 * 28 * 12 + p_month * 86400 * 28 + p_day * 86400
        if total_time - p_time > terms_list[p_term] * (86400 * 28 - 1):
            answer.append(i + 1)
    return answer
    return answer