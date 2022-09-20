from colibrie.utils import (
    intersect,
    adjust_line_lenght,
)

from colibrie.geometry import Point

from copy import deepcopy

def get_intersection_between_horizontal_and_vertical_lines(horizontal_lines, vertical_lines):
    intersections = {}
    
    vertical_lines = adjust_line_lenght(vertical_lines, "vertical")
    horizontal_lines = adjust_line_lenght(horizontal_lines, "horizontal")
    
    for horizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
            point_a, point_b = horizontal_line
            point_c, point_d = vertical_line
            intersection_point = intersect(point_a, point_b, point_c, point_d)
            if intersection_point:
                intersections[intersection_point] = [vertical_line, horizontal_line]
                
    vertical_lines = adjust_line_lenght(vertical_lines, "vertical", revert=True)
    horizontal_lines = adjust_line_lenght(horizontal_lines, "horizontal", revert=True)

    return intersections
