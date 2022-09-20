from math import inf
from colibrie.geometry import Point, Rect
import numpy as np


def is_table_rotated(data):
    total_span = 0
    rotated_span = 0
    for row in data:
        for column in row:
            if column:
                for span in column:
                    total_span += 1
                    # print(span['dir'])
                    if span['dir'] != (1, 0):
                        rotated_span += 1
            # column = column_text

    # all span are rotated inside the table
    if (rotated_span / total_span) == 1:
        return True

    return False


def extract_text_from_spans(spans):
    text = ""
    for span in spans:
        text += span["text"] + '<br>\n'  # TODO REMOVE <br> which is here for visual purpose now

    return text


class RangeMap:
    def __init__(self, dictionary, minimum=-inf, maximum=inf):
        assert dictionary
        self._dictionary = dictionary
        self.min, self.max = minimum, maximum
        self._generate_tree()

    def __delitem__(self, key):
        del self._dictionary[key]
        self._generate_tree()

    def __getitem__(self, item):
        current = self._tree
        while current:
            if item < current.lower:
                current = current.before
            elif item <= current.upper:
                return current.value
            else:
                current = current.after
        raise Exception("Tree not constructed properly")

    def __setitem__(self, key, value):
        self._dictionary[key] = value
        self._generate_tree()

    def _generate_tree(self):
        range_mapping = [(((p + c) / 2, (c + n) / 2), self._dictionary[c])
                         for p, c, n in self._iterate_keys()]
        self._tree = RangeMap.Node(range_mapping)

    def _iterate_keys(self):
        keys = sorted(self._dictionary.keys())
        return zip([self.min] + keys[:-1], keys, keys[1:] + [self.max])

    class Node:
        def __init__(self, range_mapping):
            assert range_mapping
            middle = len(range_mapping) // 2
            (self.lower, self.upper), self.value = range_mapping[middle]
            before, after = range_mapping[:middle], range_mapping[middle + 1:]
            self.before = RangeMap.Node(before) if before else None
            self.after = RangeMap.Node(after) if after else None


def intersect(p1, p2, p3, p4):
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


def adjust_line_lenght(lines, direction, revert=False):
    adjusted_lines = []

    if direction == "vertical":
        for line in lines:
            point_a = line[0]
            point_b = line[1]
            point_a.y -= 3 if not revert else -3
            point_b.y += 3 if not revert else -3

            adjusted_lines.append(
                (point_a, point_b)
            )
    elif direction == "horizontal":
        for line in lines:
            point_a = line[0]
            point_b = line[1]
            point_a.x -= 3 if not revert else -3
            point_b.x += 3 if not revert else -3

            adjusted_lines.append(
                (point_a, point_b)
            )
    else:
        return adjusted_lines

    return adjusted_lines


def is_rectangle_overlap(r1, r2):
    if (r1[0] >= r2[2]) or (r1[2] <= r2[0]) or (r1[3] <= r2[1]) or (r1[1] >= r2[3]):
        return False
    else:
        return True


def is_rectangle_contained(r1, r2):
    return r1[0] <= r2[0] <= r2[2] <= r1[2] and r1[1] <= r2[1] <= r2[3] <= r1[3]


def get_text_in_cell(rect, text):
    text_in_cell = []

    # Give a 1 px text tolerance around the rect
    rect = Rect(rect.x0 - 1, rect.y0 - 1, rect.x1 + 1, rect.y1 + 1)

    # skip block / lines that are not relevant because no intersection with the cell Rect to speed up execution times
    # by 10%
    for block in text.get('blocks'):
        bbox = block['bbox']
        if is_rectangle_overlap([bbox[0], bbox[1], bbox[2], bbox[3]], [rect.x0, rect.y0, rect.x1, rect.y1]):

            for line in block.get('lines'):
                bbox = line['bbox']
                if is_rectangle_overlap([bbox[0], bbox[1], bbox[2], bbox[3]], [rect.x0, rect.y0, rect.x1, rect.y1]):

                    for span in line.get('spans'):
                        bbox = span['bbox']

                        if is_rectangle_contained([rect.x0, rect.y0, rect.x1, rect.y1],
                                                  [bbox[0], bbox[1], bbox[2], bbox[3]]):
                            span['dir'] = line['dir']
                            text_in_cell.append(span)

    return text_in_cell


def closest_value(input_list, input_value):
    arr = np.asarray(input_list)

    i = (np.abs(arr - input_value)).argmin()

    return arr[i]
