import fitz
import pytest
import os

from colibri.geometry import Point
from colibri.lines import (
    get_lines_fragmented,
    get_horizontal_fragmented_lines,
    get_vertical_fragmented_lines,
    remove_overlaping_vertical_lines,
    remove_overlaping_horizontal_lines
)

from tests.unit.lines_assets.expected_fragmented_lines_test_1 import expected_fragmented_lines_test_1
from tests.unit.lines_assets.expected_fragmented_lines_test_2 import expected_fragmented_lines_test_2
from tests.unit.lines_assets.expected_fragmented_lines_test_3 import expected_fragmented_lines_test_3
from tests.unit.lines_assets.expected_fragmented_lines_test_4 import expected_fragmented_lines_test_4
from tests.unit.lines_assets.expected_fragmented_lines_test_5 import expected_fragmented_lines_test_5
from tests.unit.lines_assets.expected_fragmented_lines_test_6 import expected_fragmented_lines_test_6
from tests.unit.lines_assets.expected_fragmented_lines_test_7 import expected_fragmented_lines_test_7
from tests.unit.lines_assets.expected_fragmented_lines_test_empty import expected_fragmented_lines_test_empty

parent_path = os.path.dirname(os.path.dirname(__file__))


class TestLines:
    @pytest.mark.parametrize("fragmented_lines_expected, path", [
        (expected_fragmented_lines_test_1, f'{parent_path}/assets/test_1.pdf'),
        (expected_fragmented_lines_test_2, f'{parent_path}/assets/test_2.pdf'),
        (expected_fragmented_lines_test_3, f'{parent_path}/assets/test_3.pdf'),
        (expected_fragmented_lines_test_4, f'{parent_path}/assets/test_4.pdf'),
        (expected_fragmented_lines_test_5, f'{parent_path}/assets/test_5.pdf'),
        (expected_fragmented_lines_test_6, f'{parent_path}/assets/test_6.pdf'),
        (expected_fragmented_lines_test_7, f'{parent_path}/assets/test_7.pdf'),
        (expected_fragmented_lines_test_empty, f'{parent_path}/assets/empty.pdf'),
    ])
    def test_get_lines_fragmented(self, fragmented_lines_expected, path):
        doc = fitz.Document(path)

        for page in doc:
            lines = get_lines_fragmented(page)

            assert lines == fragmented_lines_expected

    def test_get_horizontal_fragmented_lines(self):
        lines = [
            (Point(70, 10), Point(70, 100)),
            (Point(70, 10), Point(70, 50)),
            (Point(70, 20), Point(100, 20)),
            (Point(7, 20), Point(40, 20)),
            (Point(10, 20), Point(150, 20)),
        ]

        expected_lines = [
            (Point(70, 20), Point(100, 20)),
            (Point(7, 20), Point(40, 20)),
            (Point(10, 20), Point(150, 20)),
        ]

        result = get_horizontal_fragmented_lines(lines)

        assert result == expected_lines

    def test_get_vertical_fragmented_lines(self):
        lines = [
            (Point(70, 10), Point(70, 100)),
            (Point(70, 10), Point(70, 50)),
            (Point(7, 20), Point(40, 20)),
            (Point(10, 20), Point(150, 20)),
        ]

        expected_lines = [
            (Point(70, 10), Point(70, 100)),
            (Point(70, 10), Point(70, 50)),
        ]

        result = get_vertical_fragmented_lines(lines)

        assert result == expected_lines

    def test_remove_overlapping_vertical_lines(self):
        lines = [
            (Point(70, 10), Point(70, 100)),
            (Point(70, 10), Point(70, 50)),
            (Point(70, 20), Point(70, 30)),
            (Point(70, 90), Point(70, 140)),
            (Point(70, 150), Point(70, 300))
        ]

        expected_lines = [
            (Point(70, 10), Point(70, 140)),
            (Point(70, 150), Point(70, 300))
        ]

        result = remove_overlaping_vertical_lines(lines)

        assert result == expected_lines

    def test_remove_overlapping_horizontal_lines(self):
        lines = [
            (Point(70, 20), Point(100, 20)),
            (Point(7, 20), Point(40, 20)),
            (Point(10, 20), Point(150, 20)),
            (Point(5, 20), Point(30, 20)),
            (Point(200, 20), Point(400, 20))
        ]

        expected_lines = [
            (Point(5, 20), Point(150, 20)),
            (Point(200, 20), Point(400, 20))
        ]

        result = remove_overlaping_horizontal_lines(lines)

        assert result == expected_lines
