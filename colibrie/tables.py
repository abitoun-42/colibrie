from typing import Union

from fitz import Rect, TEXTFLAGS_DICT, TEXT_PRESERVE_IMAGES, Page

from colibrie.geometry import Point
from colibrie.core import Table, Cell, Rotation
from ailist import AIList


def get_tables_candidates(
    vertical_segments: list[tuple[Point, Point]],
    horizontal_segments: list[tuple[Point, Point]],
) -> list[list[tuple[Point, Point]]]:
    """
    This function group segments by vertical interval then by horizontal interval
    to extract distinct group of segments from each other

    for example in this situation :

    +---------+
    |  Col1   |
    +---------+
    | Value 1 |
    +---------+

            +---------+---------+------+
            |  Col1   |  Col2   | Col3 |
            +---------+---------+------+
            | Value 1 | Value 2 |  123 |
            | Value 2 |         |      |
            +---------+---------+------+

        Page 93
        ------

    it'll result in 3 distinct tables candidates
    (2 to be exact because the line below page number
    will not be a valid table candidate)

    :param vertical_segments: list of vertical segments
    :param horizontal_segments: list of horizontal segments
    :return: List of list of segments, where each list is valid tables candidates
    """

    # get vertical intervals
    interval_tree = AIList()
    [interval_tree.add(line[0].y, line[1].y) for line in vertical_segments]

    vertical_merged_interval = interval_tree.merge(gap=1)

    tables_candidate = []
    interval_group = {}

    for vertical_interval in vertical_merged_interval:
        interval_group[vertical_interval.start, vertical_interval.end] = []

        for segment in vertical_segments:
            if (
                segment[0].y >= vertical_interval.start
                and segment[1].y <= vertical_interval.end
            ):
                interval_group[vertical_interval.start, vertical_interval.end].append(
                    segment
                )

        for segment in horizontal_segments:
            if (
                segment[0].y >= vertical_interval.start
                and segment[1].y <= vertical_interval.end
            ):
                interval_group[vertical_interval.start, vertical_interval.end].append(
                    segment
                )

        # get horizontal intervals from each group
        interval_tree = AIList()
        [
            interval_tree.add(line[0].x, line[1].x)
            for line in interval_group[vertical_interval.start, vertical_interval.end]
        ]

        horizontal_merged_interval = interval_tree.merge(gap=1)

        for horizontal_interval in horizontal_merged_interval:
            table_candidate = []

            for segment in interval_group[
                vertical_interval.start, vertical_interval.end
            ]:
                if (
                    segment[0].x >= horizontal_interval.start
                    and segment[1].x <= horizontal_interval.end
                ):
                    table_candidate.append(segment)

            # We make sure that every table candidate have at least 4 lines
            # Which is the bare minimum to create a single cell
            if len(table_candidate) > 3:
                tables_candidate.append(table_candidate)
            else:
                continue

    return tables_candidate


def create_table(
    intersections: dict[tuple[list[tuple[Point, Point]], list[tuple[Point, Point]]]],
    horizontal_segments: list[tuple[Point, Point]],
    vertical_segments: list[tuple[Point, Point]],
) -> Table:
    """
    Create a Table object from segments and intersections

    :param intersections: dict of intersections point and vertical|horizontal segments associated
    :param horizontal_segments: list of horizontal segments
    :param vertical_segments: list of vertical segments
    :return:
    """
    intersections = [
        intersection
        for intersection in sorted(intersections, key=lambda point: (point.y, point.x))
    ]

    table = Table(
        intersections=intersections,
        rect=Rect(intersections[0], intersections[-1]),
        horizontal_segments=horizontal_segments,
        vertical_segments=vertical_segments,
    )

    return table


def process_table(
    page: Page,
    table: Table,
    intersections: dict[tuple[list[tuple[Point, Point]], list[tuple[Point, Point]]]],
) -> Union[Table, None]:
    """
    This function process each Table object by finding Cell from segments coordinate and then extracting
    Text span for each Cell

    it also determine the rotation of the Table based on text orientation ratio in the Table

    Legend :
    tl => top left
    tr => top right
    bl => bottom left
    br => bottom right

    :param page: Page Object
    :param table: Table Object
    :param intersections: dict of intersections point and vertical|horizontal segments associated
    :return:
    """

    rotated_span = {Rotation.unrotated.value: 0, Rotation.rotated_90.value: 0}

    text = page.get_text(
        "dict", flags=TEXTFLAGS_DICT & ~TEXT_PRESERVE_IMAGES, clip=table.rect
    )

    # Reconstruct intersection point group by lines height as
    # list of list containing intersections point
    rows = []
    for index, row in table.intersections_df.groupby("y"):
        rows.append(row.to_dict(orient="records"))

    # Each row is a group of intersection point
    for row_index, row in enumerate(rows):
        # Stopping one row before the last row because
        # the last row is always the bottom of the table
        # and can't be used for a cell matching
        if row_index == len(rows) - 1:
            break

        tl = None
        for intersection_index, intersection in enumerate(row):
            if intersection_index == len(row) - 1:
                break

            if not tl:
                tl = intersection

            tr = row[intersection_index + 1]
            tl_intersection_line = intersections[tl["x"], tl["y"]]
            tr_intersection_line = intersections[tr["x"], tr["y"]]

            # if tl and tr point are the same horizontal_line
            if tl_intersection_line[1] == tr_intersection_line[1]:
                bl, br = find_bottom_cell_coordinate(
                    tl, tr, rows, row_index, intersections
                )
            else:
                tl = None
                continue

            # A Cell is valid only if we found tl, tr, bl and br coordinate
            if not bl and not br:
                continue

            cell = Cell(
                rect=Rect(Point(tl["x"], tl["y"]), Point(br["x"], br["y"])),
                row_size=table.row[br["y"]] - table.row[tl["y"]],
                col_size=table.col[br["x"]] - table.col[tl["x"]],
            )

            cell.get_text(text)
            for span in cell.spans:
                try:
                    rotated_span[span["dir"]] += 1
                except KeyError:
                    print(f"missing key for rotation {span['dir']}")

            table.cells[row_index].append(cell)

            # to permit the transposition of cells in order to rotate the table if needed
            # we append None value to match the size of sum(col_size) for each row
            for i in range(cell.row_size):
                for j in range(1, cell.col_size):
                    table.cells[row_index + i].append(None)

            tl = None

    # HANDLE BAD TABLE #
    total_cell = 0
    empty_cell = 0
    for row in table.cells:
        for cell in row:
            if cell:
                total_cell += 1
                if not cell.text:
                    empty_cell += 1

    empty_cell_ratio = total_cell / max(
        empty_cell, 1
    )  # prevent division by 0 if empty table

    # if there is only empty cell in the table, it is not a valid table
    if empty_cell_ratio == 1:
        return None
    else:
        table.match_row_size_sum()
        table.rotation = max(rotated_span, key=rotated_span.get)
        table.set_rotation()

    return table


def find_bottom_cell_coordinate(
    tl: dict[str],
    tr: dict[str],
    rows: list[list[dict[str]]],
    row_index: int,
    intersections: dict[tuple[list[tuple[Point, Point]], list[tuple[Point, Point]]]],
) -> Union[tuple[dict[str], dict[str]], tuple[None, None]]:
    """
    This function try to find the bottom (bl, br) coordinate of a Cell based on top (tl, tr) coordinate

    Legend :

    tl => top left
    tr => top right
    bl => bottom left
    br => bottom right

    :param tl: dict containing a x, y coordinate information
    :param tr: dict containing a x, y coordinate information
    :param rows: list of list of dict containing a x, y coordinate information representing a row in the Table
    :param row_index: Index of the current row we try to find the bottom coordinate
    :param intersections: dict of intersections point and vertical|horizontal segments associated
    :return: The bottom cell coordinate if a match is found, else None
    """
    bl = None
    br = None

    # Starting to search for corresponding bl / br at row_index + 1 because we always
    # match a row with the row below it

    # Each row is a group of intersection point
    for row in rows[row_index + 1 :]:
        for intersection in row:

            if tl["x"] <= intersection["x"] < tr["x"] and not bl:
                bl = intersection

            if intersection["x"] == tr["x"] and not br and bl:
                br = intersection

            if br and bl:
                tl_intersection_line = intersections[tl["x"], tl["y"]]
                tr_intersection_line = intersections[tr["x"], tr["y"]]

                bl_intersection_line = intersections[bl["x"], bl["y"]]
                br_intersection_line = intersections[br["x"], br["y"]]

                # if bl and br point are on the same horizontal_line
                # if tl and bl point are on the same vertical_line
                # if tr and br point are on the same vertical_line
                if (
                    bl_intersection_line[1] == br_intersection_line[1]
                    and tl_intersection_line[0] == bl_intersection_line[0]
                    and tr_intersection_line[0] == br_intersection_line[0]
                ):
                    return bl, br
                else:
                    bl = None
                    br = None

        # If we cannot find any valid candidate for closing the cell on this row, we need
        # to reset the start / end point value for the next row to None to prevent
        # Mixed row matching
        bl = None
        br = None

    return None, None
