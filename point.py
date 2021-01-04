class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z  = x, y, z

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        else:
            return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return TypeError

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return TypeError

    def __mul__(self, other):
        if str(other).isdigit():
            return Point(self.x * other, self.y * other, self.z * other)
        else:
            return TypeError

    def __rmul__(self, other):
        if str(other).isdigit():
            return Point(self.x * other, self.y * other, self.z * other)
        else:
            return TypeError

    def __floordiv__(self, other):
        if str(other).isdigit():
            if other != 0:
                return Point(self.x // other, self.y // other, self.z // other)
            else:
                return ZeroDivisionError
        else:
            return TypeError

    def __truediv__ (self, other):
        if str(other).isdigit():
            if other != 0:
                return Point(self.x / other, self.y / other, self.z / other)
            else:
                return ZeroDivisionError
        else:
            return TypeError

    def __iter__(self):
        return iter((self.x, self.y, self.z))

