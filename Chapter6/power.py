def is_power(a,b):
    if a%b == 0:
        return True
    else:
        return False
    return is_power((a/b),b)
    
