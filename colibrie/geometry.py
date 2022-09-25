class Rect:
    """
    Class Object to represent a Rectangle coordinates
    """

    def __init__(self, x0: float, y0: float, x1: float, y1: float):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1

    def __getitem__(self, i):
        return (self.x0, self.y0, self.x1, self.y1)[i]

    def __len__(self):
        return 4

    def __repr__(self):
        return "Rect" + str(tuple(self))


class Point:
    """
    Class Object to represent a Point coordinates
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __getitem__(self, i):
        return (self.x, self.y)[i]

    def __len__(self):
        return 2

    def __repr__(self):
        return "Point" + str(tuple(self))

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __bool__(self):
        return not (max(self) == min(self) == 0)

    def __nonzero__(self):
        return not (max(self) == min(self) == 0)

    def __eq__(self, p):
        if not hasattr(p, "__len__"):
            return False
        return len(p) == 2 and bool(self - p) is False

    def __sub__(self, p):
        if hasattr(p, "__float__"):
            return Point(self.x - p, self.y - p)
        if len(p) != 2:
            raise ValueError("Point: bad seq len")
        return Point(self.x - p[0], self.y - p[1])

    def __hash__(self):
        return hash(tuple(self))
