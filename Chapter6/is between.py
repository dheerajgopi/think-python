def compare(x,y):
    if x > y:
        return 1
    if x < y:
        return -1
    else:
        return 0

def is_between(x,y,z):
    if x <= y and y <=z:
        print 'ok'
    else:
        print 'not ok'
