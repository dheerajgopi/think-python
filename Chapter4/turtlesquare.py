from swampy.TurtleWorld import *

def square(t):
    world = TurtleWorld()
    t = Turtle()

    for i in range(4):
        fd(t,100)
        lt(t)

    wait_for_user()

square("bob")


