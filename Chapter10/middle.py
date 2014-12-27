def middle(lst):
    midlist = lst
    i = len(midlist)-2
    del midlist[0]
    del midlist[i]
    return midlist
