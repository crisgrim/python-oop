class Color():
    # Properties
    red = 'Red'
    green = 'Green'
    blue = 'Blue'
    current = ''

    # Constructor
    def __init__(self, color):
        self.current = color


class Point2D():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinate2D(self):
        return [self.x, self.y]


class Point3D(Point2D, Color):
    z = 0

    def __init__(self, x, y, z, color):
        Point2D.__init__(self, x, y)
        Color.__init__(self, color)
        self.z = z

    def coordinate3D(self):
        return [self.x, self.y, self.z, self.current]


point1 = Point2D(10, 20)
point2 = Point3D(50, 50, 5, 'black')

print(point1.coordinate2D())
print(point2.coordinate2D())
print(point2.coordinate3D())
