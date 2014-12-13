def do_twice(f,s):
    f(s)
    f(s)

def print_spam(s):
    print s

do_twice(print_spam,"qwertyuiop")
