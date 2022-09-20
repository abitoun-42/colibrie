class Rect:
    """Rect() - all zeros
    Rect(x0, y0, x1, y1) - 4 coordinates
    """

    def __init__(self, x0, y0, x1, y1):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        return None

    def __getitem__(self, i):
        return (self.x0, self.y0, self.x1, self.y1)[i]

    def __len__(self):
        return 4

    def __repr__(self):
        return "Rect" + str(tuple(self))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, i):
        return (self.x, self.y)[i]

    def __len__(self):
        return 2

    def __setitem__(self, i, v):
        v = float(v)
        if i == 0:
            self.x = v
        elif i == 1:
            self.y = v
        else:
            raise IndexError("index out of range")
        return None

    def __repr__(self):
        return "Point" + str(tuple(self))

    def __pos__(self):
        return Point(self)

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
