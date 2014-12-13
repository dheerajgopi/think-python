def do_twice(s):
    print s
    print s
    
def do_four(g,s):
    g(s)
    g(s)

do_four(do_twice,"abcd")
    
