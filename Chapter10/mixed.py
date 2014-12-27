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
