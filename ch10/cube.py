import math

class Cube:
    """This class can return the volume and the
    surface area of a cube."""

    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surfaceArea(self):
        return 6 * self.side ** 2