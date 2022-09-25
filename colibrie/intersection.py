from colibrie.geometry_operation import intersect
from colibrie.segments import adjust_segments_length


def get_intersection_between_horizontal_and_vertical_lines(
    horizontal_lines, vertical_lines
):
    intersections = {}

    adjust_segments_length(vertical_lines, "vertical")
    adjust_segments_length(horizontal_lines, "horizontal")

    for horizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
            point_a, point_b = horizontal_line
            point_c, point_d = vertical_line
            intersection_point = intersect(point_a, point_b, point_c, point_d)
            if intersection_point:
                intersections[intersection_point] = [vertical_line, horizontal_line]

    adjust_segments_length(vertical_lines, "vertical", revert=True)
    adjust_segments_length(horizontal_lines, "horizontal", revert=True)

    return intersections
