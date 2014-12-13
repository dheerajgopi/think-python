def square_root(a):
    epsilon = 0.0000001
    x=a/(2.0**a)
    y=(x+(a/x))/2
    if abs(y-x) > epsilon:
        x=y
        square_root(x)
    else:
        print x
