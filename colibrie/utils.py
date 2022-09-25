import numpy as np

from colibrie.geometry import Rect
from colibrie.geometry_operation import is_rectangle_overlap, is_rectangle_contained


def extract_text_from_spans(spans):
    text = ""
    for span in spans:
        text += (
            span["text"] + "<br>\n"
        )  # TODO REMOVE <br> which is here for visual purpose now

    return text


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
