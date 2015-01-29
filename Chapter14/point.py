from point1 import *
import math
import copy

def distance_between_points(p1,p2):
    '''To calculate the distance between 2 points'''
    distance = math.sqrt(((p1.x - p2.x)**2) + ((p1.y - p2.y)**2))
    return distance

def move_rectangle(rect,dx,dy):
    '''To move the rectangle by its corner'''
    new_rect = copy.deepcopy(rect)
    new_rect.width = rect.width
    new_rect.height = rect.height
    new_rect.corner = Point()
    new_rect.corner.x = rect.corner.x + dx
    new_rect.corner.y = rect.corner.y + dy
    print_point(new_rect.corner)
    return new_rect
