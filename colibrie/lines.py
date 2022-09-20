import math

from ailist import AIList

from colibrie.utils import (
    RangeMap,
    closest_value
)

from colibrie.geometry import Rect, Point


def get_lines_fragmented(page):
    lines_fragmented = []

    drawings = page.get_cdrawings()

    for drawing in drawings:
        # If there is a curve in the drawing, we considere it not valid for a rectangle
        for part in drawing['items']:
            if part[0] == 'c':
                break
        else:
            # By default if the key closePath is not present, it's a segment
            # so it's not a closePath
            if drawing.get("closePath", False):
                continue

            rect = drawing['rect']
            rect = Rect(rect[0], rect[1], rect[2], rect[3])
            if math.isclose(rect.x0, rect.x1, abs_tol=3):
                rect.x1 = rect.x0
            if math.isclose(rect.y0, rect.y1, abs_tol=3):
                rect.y1 = rect.y0

            rect.x0 = round(rect.x0) if rect.x0 > 0 else 0
            rect.x1 = round(rect.x1) if rect.x1 > 0 else 0
            rect.y0 = round(rect.y0) if rect.y0 > 0 else 0
            rect.y1 = round(rect.y1) if rect.y1 > 0 else 0

            upper_line = (Point(rect.x0, rect.y0), Point(rect.x1, rect.y0))
            lower_line = (Point(rect.x0, rect.y1), Point(rect.x1, rect.y1))
            left_line = (Point(rect.x0, rect.y0), Point(rect.x0, rect.y1))
            right_line = (Point(rect.x1, rect.y0), Point(rect.x1, rect.y1))

            lines_fragmented += [upper_line, lower_line, left_line, right_line]

    return lines_fragmented


def get_vertical_fragmented_lines(lines_fragmented):
    return [line for line in lines_fragmented if
            math.isclose(line[0].x, line[1].x, abs_tol=5) and line[0].y != line[1].y]


def get_horizontal_fragmented_lines(lines_fragmented):
    return [line for line in lines_fragmented if
            math.isclose(line[0].y, line[1].y, abs_tol=5) and line[0].x != line[1].x]


def generate_missing_horizontal_lines(horizontal_lines, vertical_lines, distinct_x_lst, distinct_y_lst, range_x,
                                      range_y):
    if not horizontal_lines or not vertical_lines:
        return horizontal_lines

    # Maybe we can just brutforce and recreate all the line without check
    # GET MIN MAX WIDTH HORIZONTAL LIMIT OF THE TABLE

    y_aligned_point = {y: [] for y in distinct_y_lst}

    if not y_aligned_point:
        return horizontal_lines

    range_map = RangeMap(y_aligned_point)
    for l in vertical_lines:
        for point in l:
            range_map[point.y].append(point)

    # WE HAD TO USE COPY BECAUSE OF BINARY TREE STRUCTURE WHICH PASS THE REFERENCE VALUE OTHERWISE
    for y, points in range_map._dictionary.items():
        if len(points) > 1:
            # point_a = Point(range_x[0], points[0].y)
            # point_b = Point(range_x[1], points[-1].y)
            point_a = Point(points[0].x, points[0].y)
            point_b = Point(points[-1].x, points[-1].y)
            horizontal_lines.append((point_a, point_b))

    horizontal_lines = remove_overlaping_horizontal_lines(horizontal_lines)

    return horizontal_lines


def generate_missing_vertical_lines(horizontal_lines, vertical_lines, distinct_x_lst, distinct_y_lst, range_x, range_y):
    if not horizontal_lines or not vertical_lines:
        return vertical_lines

    x_aligned_point = {x: [] for x in distinct_x_lst}

    if not x_aligned_point:
        return vertical_lines

    range_map = RangeMap(x_aligned_point)
    for l in horizontal_lines:
        for point in l:
            range_map[point.x].append(point)

    # WE HAD TO USE COPY BECAUSE OF BINARY TREE STRUCTURE WHICH PASS THE REFERENCE VALUE OTHERWISE
    for x, points in range_map._dictionary.items():
        if len(points) > 1:
            # point_a = Point(points[0].x, range_y[0])
            # point_b = Point(points[-1].x, range_y[1])
            point_a = Point(points[0].x, points[0].y)
            point_b = Point(points[-1].x, points[-1].y)
            vertical_lines.append((point_a, point_b))

    vertical_lines = remove_overlaping_vertical_lines(vertical_lines)

    return vertical_lines


def remove_overlaping_vertical_lines(vertical_lines):
    merged_vertical_lines = []

    vertical_lines.sort(key=lambda line: line[1].x)

    group = []
    current_x = None
    for line in vertical_lines:
        if not current_x:
            current_x = line[0].x
            group.append(line)
            continue

        if line[0].x != current_x:
            interval_tree = AIList()
            [interval_tree.add(line[0].y, line[1].y) for line in group]

            merged_interval = interval_tree.merge(gap=5)

            merged_vertical_lines += [(Point(current_x, interval.start), Point(current_x, interval.end)) for interval in
                                      merged_interval]
            group = [line]
            current_x = line[0].x
        else:
            group.append(line)

    if group:
        interval_tree = AIList()
        [interval_tree.add(line[0].y, line[1].y) for line in group]
        merged_interval = interval_tree.merge(gap=5)
        merged_vertical_lines += [(Point(current_x, interval.start), Point(current_x, interval.end)) for interval in
                                  merged_interval]

    return merged_vertical_lines


def remove_overlaping_horizontal_lines(horizontal_lines):
    merged_horizontal_lines = []

    horizontal_lines.sort(key=lambda line: (line[1].y))

    group = []
    current_y = None
    for line in horizontal_lines:
        if not current_y:
            current_y = line[0].y
            group.append(line)
            continue

        if line[0].y != current_y:
            interval_tree = AIList()
            [interval_tree.add(line[0].x, line[1].x) for line in group]

            merged_interval = interval_tree.merge(gap=5)

            merged_horizontal_lines += [(Point(interval.start, current_y), Point(interval.end, current_y)) for interval
                                        in
                                        merged_interval]
            group = [line]
            current_y = line[0].y
        else:
            group.append(line)

    if group:
        interval_tree = AIList()
        [interval_tree.add(line[0].x, line[1].x) for line in group]
        merged_interval = interval_tree.merge(gap=5)
        merged_horizontal_lines += [(Point(interval.start, current_y), Point(interval.end, current_y)) for interval in
                                    merged_interval]

    return merged_horizontal_lines


def normalize_vertical_lines(vertical_lines, horizontal_lines):
    """
        This function will normalize coordinate between horizontal and vertical lines
        like if a vertical line that in y = 87 and the horizontal lines corresponding has 
        a y = 86 then the vertical line will have this y value set to 86 by calculating
        the closest Y value from horizontal lines
    """
    distinct_horizontal_y = list(
        set([point.y for lines in horizontal_lines for point in lines])
    )

    for vertical_line in vertical_lines:
        closest_y0 = closest_value(distinct_horizontal_y, vertical_line[0].y)
        closest_y1 = closest_value(distinct_horizontal_y, vertical_line[1].y)
        vertical_line[0].y = closest_y0 if math.isclose(vertical_line[0].y, closest_y0, abs_tol=3) else vertical_line[
            0].y
        vertical_line[1].y = closest_y1 if math.isclose(vertical_line[1].y, closest_y1, abs_tol=3) else vertical_line[
            1].y

    return vertical_lines


def normalize_horizontal_lines(vertical_lines, horizontal_lines):
    """
        This function will normalize coordinate between horizontal and vertical lines
        like if a vertical line that in y = 87 and the horizontal lines corresponding has 
        a y = 86 then the vertical line will have this y value set to 86 by calculating
        the closest Y value from horizontal lines
    """
    distinct_vertical_x = list(
        set([point.x for lines in vertical_lines for point in lines])
    )

    for horizontal_line in horizontal_lines:
        closest_x0 = closest_value(distinct_vertical_x, horizontal_line[0].x)
        closest_x1 = closest_value(distinct_vertical_x, horizontal_line[1].x)
        horizontal_line[0].x = closest_x0 if math.isclose(horizontal_line[0].x, closest_x0, abs_tol=3) else \
        horizontal_line[0].x
        horizontal_line[1].x = closest_x1 if math.isclose(horizontal_line[1].x, closest_x1, abs_tol=3) else \
        horizontal_line[1].x

    return horizontal_lines
