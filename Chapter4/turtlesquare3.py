from swampy.TurtleWorld import *
world = TurtleWorld()

def square(t,length,n):
    t = Turtle()

    for i in range(n):
        fd(t,length)
        rt(t,(360/n))

    wait_for_user()

square('t',50,10)
