import pandas as pd
import io
import random

from colibrie.utils import (
    get_text_in_cell,
    extract_text_from_spans,
)

from PIL import Image, ImageDraw

from enum import Enum


class Table(object):
    """
    Defines a table with coordinates relative to a left-bottom
    origin. (PDF coordinate space)
    """

    def __init__(self, intersections, rect, horizontal_segments, vertical_segments):
        self.rotation = None
        self.rect = rect
        self.intersections = intersections

        self.intersections_df = pd.DataFrame(
            [[point.x, point.y] for point in self.intersections], columns=["x", "y"]
        )

        self.horizontal_lines = horizontal_segments
        self.vertical_lines = vertical_segments

        self.row = {
            row: index
            for index, row in enumerate(
                sorted(self.intersections_df.y.unique().tolist())
            )
        }
        self.col = {
            col: index
            for index, col in enumerate(
                sorted(self.intersections_df.x.unique().tolist())
            )
        }

        self.cells = [[] for r in range(len(self.row) - 1)]

        self.debug = Debug(self)

    def set_rotation(self):
        if self.rotation == Rotation.rotated_90.value:
            # Transpose table cell
            self.cells = list(zip(*reversed(self.cells)))

            # Invert row and col size which is a consequence of the transpose
            for row in self.cells:
                for cell in row:
                    if cell:
                        cell.row_size, cell.col_size = cell.col_size, cell.row_size

    def match_row_size_sum(self):
        # to permit the transposition of cells in order to rotate the table if needed
        # we append None value to match the size of sum(row_size) for each row
        try:
            for col_index in range(
                len(max(self.cells, key=len))
            ):  # this row get the maximum lenght of inner list in cells 2d array
                for row_index, row in enumerate(self.cells):
                    cell = row[col_index]
                    if cell:
                        for i in range(1, cell.row_size):
                            self.cells[row_index + i].insert(col_index, None)
        except IndexError:
            pass

    def to_html(self):
        # transposed_cells = list(zip(*self.cells)) # 180 degree turn
        # transposed_cells = list(zip(*[reversed(row) for row in self.cells])) # 270 degree turn
        html = "<table>"
        for row in self.cells:
            html += "<tr>"
            for cell in row:
                if cell:
                    rowspan = f"rowspan={cell.row_size}"
                    colspan = f"colspan={cell.col_size}"
                    html += f'<td style="text-align:center;" {rowspan} {colspan}>{cell.text}</td>'
            html += "</tr>"
        html += "</table>"

        return html

    def to_df(self):
        data = []
        for row in self.cells:
            row_data = []
            for cell in row:
                if cell:
                    row_data.append(cell.text)
                else:
                    row_data.append(pd.NA)
            data.append(row_data)

        return pd.DataFrame(data)


class Cell(object):
    """Defines a cell in a table with coordinates relative to a
    left-bottom origin. (PDF coordinate space)

    Parameters
    ----------
    rect : fitz.Rect object
    height : height in row count
    widht : widht in column count
    text : string
        Text assigned to cell.

    """

    def __init__(self, rect, row_size, col_size):
        self.rect = rect
        self.spans = None
        self.row_size = row_size
        self.col_size = col_size
        self.text = None

    def get_text(self, text):
        self.spans = get_text_in_cell(rect=self.rect, text=text)
        self.text = extract_text_from_spans(self.spans)

    def __repr__(self):
        return repr(self.text)


class Rotation(Enum):
    unrotated = (1.0, 0.0)
    rotated_90 = (0.0, -1.0)


class Debug:
    def __init__(self, table: Table, img_bytes: bytes = None):
        self.table = table
        self.image = img_bytes

    def show_cells(self, as_bytes: bool = True, image: bytes = None):
        if not self.image:
            print("Please ensure that the debug mode is activated")
            return

        with Image.open(io.BytesIO(image if image else self.image)) as img:
            draw = ImageDraw.Draw(img)

            for row in self.table.cells:
                for cell in row:
                    if cell:
                        color = (
                            int(random.uniform(30, 255)),
                            int(random.uniform(30, 255)),
                            int(random.uniform(30, 255)),
                        )
                        draw.rectangle(
                            [cell.rect.x0, cell.rect.y0, cell.rect.x1, cell.rect.y1],
                            outline=color,
                            width=2,
                        )

            if as_bytes:
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format=img.format)
                imgByteArr = imgByteArr.getvalue()

                return imgByteArr
            else:
                img.show()

    def show_border(self, as_bytes: bool = True, image: bytes = None):
        if not self.image:
            print("Please ensure that the debug mode is activated")
            return

        with Image.open(io.BytesIO(image if image else self.image)) as img:
            draw = ImageDraw.Draw(img)

            draw.rectangle(
                [
                    self.table.rect.x0,
                    self.table.rect.y0,
                    self.table.rect.x1,
                    self.table.rect.y1,
                ],
                outline=(0, 128, 0),
                width=2,
            )

            if as_bytes:
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format=img.format)
                imgByteArr = imgByteArr.getvalue()

                return imgByteArr
            else:
                img.show()

    def show_intersections(self, as_bytes: bool = True, image: bytes = None):
        if not self.image:
            print("Please ensure that the debug mode is activated")
            return

        with Image.open(io.BytesIO(image if image else self.image)) as img:
            draw = ImageDraw.Draw(img)

            for intersection in self.table.intersections:
                tl = (intersection.x - 3, intersection.y - 3)
                br = (intersection.x + 3, intersection.y + 3)
                coordinate = [tl, br]
                draw.ellipse(coordinate, outline=(255, 0, 0), width=2)

            if as_bytes:
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format=img.format)
                imgByteArr = imgByteArr.getvalue()

                return imgByteArr
            else:
                img.show()

    def show_lines(self, as_bytes: bool = True, image: bytes = None):
        if not self.image:
            print("Please ensure that the debug mode is activated")
            return

        with Image.open(io.BytesIO(image if image else self.image)) as img:
            draw = ImageDraw.Draw(img)

            lines = self.table.horizontal_lines + self.table.vertical_lines

            for line in lines:
                color = (
                    int(random.uniform(30, 255)),
                    int(random.uniform(30, 255)),
                    int(random.uniform(30, 255)),
                )
                draw.line(
                    [line[0].x, line[0].y, line[1].x, line[1].y], fill=color, width=2
                )

            if as_bytes:
                imgByteArr = io.BytesIO()
                img.save(imgByteArr, format=img.format)
                imgByteArr = imgByteArr.getvalue()

                return imgByteArr
            else:
                img.show()
