"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return '(%d, %d)' %(self.x,self.y)


    def __add__(self,other):
        if isinstance(other, tuple):
            return self.x + other[0] , self.y + other[1]
        else:
            return self.x + other.x , self.y + other.y


    def print_point(p):
        """Print a Point object in human-readable format."""
        print '(%g, %g)' % (p.x, p.y)


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


    def find_center(rect):
        """Returns a Point at the center of a Rectangle."""
        p = Point()
        p.x = rect.corner.x + rect.width/2.0
        p.y = rect.corner.y + rect.height/2.0
        return p


    def grow_rectangle(rect, dwidth, dheight):
        """Modify the Rectangle by adding to its width and height.

        rect: Rectangle object.
        dwidth: change in width (can be negative).
        dheight: change in height (can be negative).
        """
        rect.width += dwidth
        rect.height += dheight


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height


if __name__ == '__main__':
    main()

