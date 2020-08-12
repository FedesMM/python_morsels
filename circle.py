import math


class Circle:
    def __init__(self, radius=1):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError('radius cannot be negative')
    
    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError('radius cannot be negative')

    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, diameter):
        if diameter >= 0:
            self._radius = diameter/2
        else:
            raise ValueError('radius cannot be negative')

    @property
    def area(self):
        return math.pi * float(pow(self.radius, 2))


