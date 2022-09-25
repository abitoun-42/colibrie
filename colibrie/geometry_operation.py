from typing import Union

from colibrie.geometry import Point


def intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> Union[Point, None]:
    """
    This function determine is there is an intersection between 2 segments

    Segment(P1, P2) and Segment (P3, P4)
    :param p1: Starting Point Object containing x, y coordinate for segment 1
    :param p2: Ending Point Object containing x, y coordinate for segment 1
    :param p3: Starting Point Object containing x, y coordinate for segment 2
    :param p4: Ending Point Object containing x, y coordinate for segment 2
    :return: Point of intersection if exist, else None
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return Point(x, y)


def is_rectangle_overlap(
    r1: tuple[float, float, float, float], r2: tuple[float, float, float, float]
) -> bool:
    """
    This function determine if two rectangle overlap

    :param r1: Rectangle 1
    :param r2: Rectangle 2
    :return: True if r1 and r2 overlap else False
    """
    if (r1[0] >= r2[2]) or (r1[2] <= r2[0]) or (r1[3] <= r2[1]) or (r1[1] >= r2[3]):
        return False
    else:
        return True


def is_rectangle_contained(
    r1: tuple[float, float, float, float], r2: tuple[float, float, float, float]
) -> bool:
    """
    This function determine if rectangle r1 is contained in rectangle r2

    :param r1: Rectangle 1
    :param r2: Rectangle 2
    :return: True if r1 contains r2 else False
    """
    return r1[0] <= r2[0] <= r2[2] <= r1[2] and r1[1] <= r2[1] <= r2[3] <= r1[3]
