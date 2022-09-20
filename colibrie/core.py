import pandas as pd

from colibrie.utils import (
    get_text_in_cell,
    extract_text_from_spans,
)

from enum import Enum


class TableList(object):
    """Defines a list of core.Table objects. Each table can
    be accessed using its index.

    Attributes
    ----------
    n : int
        Number of tables in the list.

    """

    def __init__(self, tables):
        self._tables = tables

    def __repr__(self):
        return f"<{self.__class__.__name__} n={self.n}>"

    def __len__(self):
        return len(self._tables)

    def __getitem__(self, idx):
        return self._tables[idx]

    @property
    def n(self):
        return len(self)


class Table(object):
    """Defines a table with coordinates relative to a left-bottom
    origin. (PDF coordinate space)

    Parameters
    ----------
    cols : list
        List of tuples representing column x-coordinates in increasing
        order.
    rows : list
        List of tuples representing row y-coordinates in decreasing
        order.

    Attributes
    ----------
    df : :class:`pandas.DataFrame`
    shape : tupl
        Shape of the table.
    accuracy : float
        Accuracy with which text was assigned to the cell.
    whitespace : float
        Percentage of whitespace in the table.
    order : int
        Table number on PDF page.
    page : int
        PDF page number.

    """

    def __init__(self, intersections, rect, horizontal_lines, vertical_lines):
        self.rect = rect
        self.intersections = intersections

        self.intersections_df = pd.DataFrame([[point.x, point.y] for point in self.intersections], columns=["x", "y"])

        self.horizontal_lines = horizontal_lines
        self.vertical_lines = vertical_lines
        self.row = {row: index for index, row in enumerate(sorted(self.intersections_df.y.unique().tolist()))}
        self.col = {col: index for index, col in enumerate(sorted(self.intersections_df.x.unique().tolist()))}

        self.cells = [[] for r in range(len(self.row) - 1)]

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
                    len(max(self.cells, key=len))):  # this row get the maximum lenght of inner list in cells 2d array
                for row_index, row in enumerate(self.cells):
                    cell = row[col_index]
                    if cell:
                        for i in range(1, cell.row_size):
                            self.cells[row_index + i].insert(col_index, None)
        except IndexError:
            pass

    def to_html(self):
        import random
        # transposed_cells = list(zip(*self.cells)) # 180 degree turn
        # transposed_cells = list(zip(*[reversed(row) for row in self.cells])) # 270 degree turn
        html = '<table>'
        for row in self.cells:
            html += "<tr>"
            for cell in row:
                if cell:
                    rowspan = f'rowspan={cell.row_size}'
                    colspan = f'colspan={cell.col_size}'
                    # color = "%06x" % random.randint(0, 0xFFFFFF)
                    html += f'<td style="text-align:center;" {rowspan} {colspan}>{cell.text}</td>'
            html += "</tr>"
        html += "</table>"

        return html

    def to_df(self):
        return pd.read_html(self.to_html())[0]


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
