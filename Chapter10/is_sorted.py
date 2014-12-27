def ascending(lst):
    i=0
    while i<len(lst):
        if lst[i]>lst[i+1]:
            return False
    return True
    
def descending(lst):
    i=0
    while i<len(lst):
        if lst[i]<lst[i+1]:
            return False
    return True

def mixed(lst):
    a=0
    b=0
    for i in lst:
        if type(i) is int or type(int) is float:
            a=1
        elif type(i) is str:
            b=1
    if a==1 and b==1:
        return True
    else:
        return False

def is_sorted(lst):
    if mixed(lst) is True:
        return "Mixture of Numbers & Strings"
    elif ascending(lst) is True:
        return "Ascending"
    elif descending(lst) is True:
        return "Descending"
    else:
        return "No Particular Order"
