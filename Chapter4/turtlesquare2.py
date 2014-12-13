from swampy.TurtleWorld import *

def square(t, length):
    world = TurtleWorld()
    t = Turtle()
    for i in range(4):
        fd(t, length)
        lt(t)

    wait_for_user()

square('t', 300)
