def cumulative_sum(lst):
    clst = []
    sum = 0
    i = 0
    while i < len(lst):
        sum += lst[i]
        clst.append(sum)
        i += 1
    return clst
