# defining a function to draw a square

def draw_square():
    a = "+ - - - - + - - - - +"
    b = "/         /         /"
    print a
    print b
    print b
    print b
    print b
    print a
    print b
    print b
    print b
    print b
    print a

draw_square()

def draw_4square():
    draw_square()
    draw_square()

draw_4square()
