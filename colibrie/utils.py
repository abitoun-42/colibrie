from typing import Union

import numpy as np

from colibrie.geometry import Rect
from colibrie.geometry_operation import is_rectangle_overlap, is_rectangle_contained


def extract_text_from_spans(spans: dict) -> str:
    """
    This function will extract text information from spans

    :param spans: list of dict containing all information about the text of a cell
                  like coordinate, orientation, fonts, size
                  refer to https://pymupdf.readthedocs.io/en/latest/textpage.html#structure-of-dictionary-outputs
    :return: Text of a cell as a string
    """
    text = ""
    for span in spans:
        text += (
            span["text"] + "<br>\n"
        )  # TODO REMOVE <br> which is here for visual purpose now

    return text


def get_text_in_cell(rect: Rect, text: list[dict]) -> list[dict]:
    """
    This function select all span of text that are contained into a cell coordinate from a list of text spans

    :param rect: a rect clip where we search for the text
    :param text: a list of dicts extracted from page
                 refer to https://pymupdf.readthedocs.io/en/latest/textpage.html#TextPage.extractDICT
                 for more information
    :return: list of dict where each one represent a text span
    """
    text_in_cell = []

    # Give a 1 px text tolerance around the rect
    rect = Rect(rect.x0 - 1, rect.y0 - 1, rect.x1 + 1, rect.y1 + 1)

    # skip block / lines that are not relevant because no intersection with the cell Rect to speed up execution times
    # by 10%
    for block in text.get("blocks"):
        bbox = block["bbox"]
        if is_rectangle_overlap(
            (bbox[0], bbox[1], bbox[2], bbox[3]), (rect.x0, rect.y0, rect.x1, rect.y1)
        ):

            for line in block.get("lines"):
                bbox = line["bbox"]
                if is_rectangle_overlap(
                    (bbox[0], bbox[1], bbox[2], bbox[3]),
                    (rect.x0, rect.y0, rect.x1, rect.y1),
                ):

                    for span in line.get("spans"):
                        bbox = span["bbox"]

                        if is_rectangle_contained(
                            (rect.x0, rect.y0, rect.x1, rect.y1),
                            (bbox[0], bbox[1], bbox[2], bbox[3]),
                        ):
                            span["dir"] = line["dir"]
                            text_in_cell.append(span)

    return text_in_cell


def closest_value(
    input_list: list[Union[float, int]], input_value: Union[float, int]
) -> Union[float, int]:
    """
    This function return the closest value to input_value from input_list

    :param input_list: The list of number you want to find the closest value from
    :param input_value: The number you want to find the closest value
    :return: Closest value from input_list to input_value
    """
    arr = np.asarray(input_list)

    i = (np.abs(arr - input_value)).argmin()

    return arr[i]
