def nested_sum(lst):
    total = 0
    for i in range (0,len(lst)):
        if type(lst[i]) is list:
            lst[i] = sum(lst[i])
    return(sum(lst))
        
