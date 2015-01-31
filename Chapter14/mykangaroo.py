class kangaroo(object):
    """attributes : pouch_contents"""
    def __init__(self,pouch_contents = []):
        self.pouch_contents = pouch_contents


    def __str__(self):
        pouch = ['Kangaroo' + ': ']
        for i in self.pouch_contents:
            pouch.append(' ' + str(i))
        return pouch


    def put_in_pouch(self,item):
        self.pouch_contents.append(item)


    def print_pouch(self):
        print self.pouch_contents
