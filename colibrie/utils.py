import numpy as np

from math import inf
from colibrie.geometry import Rect
from colibrie.geometry_operation import is_rectangle_overlap, is_rectangle_contained


def extract_text_from_spans(spans):
    text = ""
    for span in spans:
        text += (
                span["text"] + "<br>\n"
        )  # TODO REMOVE <br> which is here for visual purpose now

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
        range_mapping = [
            (((p + c) / 2, (c + n) / 2), self._dictionary[c])
            for p, c, n in self._iterate_keys()
        ]
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


def get_text_in_cell(rect, text):
    text_in_cell = []

    # Give a 1 px text tolerance around the rect
    rect = Rect(rect.x0 - 1, rect.y0 - 1, rect.x1 + 1, rect.y1 + 1)

    # skip block / lines that are not relevant because no intersection with the cell Rect to speed up execution times
    # by 10%
    for block in text.get("blocks"):
        bbox = block["bbox"]
        if is_rectangle_overlap(
                [bbox[0], bbox[1], bbox[2], bbox[3]], [rect.x0, rect.y0, rect.x1, rect.y1]
        ):

            for line in block.get("lines"):
                bbox = line["bbox"]
                if is_rectangle_overlap(
                        [bbox[0], bbox[1], bbox[2], bbox[3]],
                        [rect.x0, rect.y0, rect.x1, rect.y1],
                ):

                    for span in line.get("spans"):
                        bbox = span["bbox"]

                        if is_rectangle_contained(
                                [rect.x0, rect.y0, rect.x1, rect.y1],
                                [bbox[0], bbox[1], bbox[2], bbox[3]],
                        ):
                            span["dir"] = line["dir"]
                            text_in_cell.append(span)

    return text_in_cell


def closest_value(input_list, input_value):
    arr = np.asarray(input_list)

    i = (np.abs(arr - input_value)).argmin()

    return arr[i]
