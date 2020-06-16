# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (0, 0)
coordinate2 = (10, 10)
l1 = Line(coordinate1, coordinate2)
print('Distance is : %s' % l1.distance())
print('Slope is : %s' % l1.slope())


# Fill in the class

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2

    def surface_area(self):
        top = 3.14 * (self.radius) ** 2
        return (2 * top) + (self.height * 2 * 3.14 * self.radius)


c1 = Cylinder(10, 10)
c2 = Cylinder(2, 3)
for cyl in [c1, c2]:
    print('The cylinder with height: %s and radius: %s, has volume: %s and surface area: %s' % (cyl.height, cyl.radius, cyl.volume(),cyl.surface_area()))
print(c1.volume())