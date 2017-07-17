import math

class Sphere:
    """This class represents a geometric solid sphere.
    It can return the radius of a sphere, the surface area,
    and volume."""
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * (self.getRadius() ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.getRadius() ** 3)