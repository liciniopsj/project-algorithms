def study_schedule(permanence_periods, target_time):
    if not isinstance(target_time, int):
        return None

    count = 0
    # percorre os períodos de permanência representados na lista
    # verifica para garantir que start e end não sejam None e
    # sejam Int
    # melhor que um monte de if, eu acho
    # 10.14s, tentar melhorar depois
    for start, end in permanence_periods:
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        if start <= target_time <= end:
            count += 1
    return count
