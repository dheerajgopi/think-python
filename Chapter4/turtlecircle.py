from swampy.TurtleWorld import *
import math
world = TurtleWorld()

def polygon(t,length,n):
    t = Turtle()
    t.delay = 0.01
    for i in range(n):
        fd(t,length)
        rt(t,(360/n))
    wait_for_user()

def circle(t,r):
    circumference = 2 * math.pi * r
    n=int(circumference/3) + 1
    length = circumference / n
    polygon(t,length,n)

circle('bob',50)
