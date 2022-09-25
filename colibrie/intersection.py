from colibrie.geometry import Point
from colibrie.geometry_operation import intersect
from colibrie.segments import adjust_segments_length


def get_intersections(
    horizontal_segments: list[tuple[Point, Point]],
    vertical_segments: list[tuple[Point, Point]],
) -> dict[tuple[list[tuple[Point, Point]], list[tuple[Point, Point]]]]:
    """
    This function find every intersections point between horizontal and
    vertical segments

    :param horizontal_segments: list of horizontal segments
    :param vertical_segments: list of vertical segments
    :return: dict of intersections point and vertical|horizontal segments associated
    """
    intersections = {}

    adjust_segments_length(vertical_segments, "vertical")
    adjust_segments_length(horizontal_segments, "horizontal")

    for horizontal_segment in horizontal_segments:
        for vertical_segment in vertical_segments:
            point_a, point_b = horizontal_segment
            point_c, point_d = vertical_segment
            intersection_point = intersect(point_a, point_b, point_c, point_d)
            if intersection_point:
                intersections[intersection_point] = (
                    vertical_segment,
                    horizontal_segment,
                )

    adjust_segments_length(vertical_segments, "vertical", revert=True)
    adjust_segments_length(horizontal_segments, "horizontal", revert=True)

    return intersections
