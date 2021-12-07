from ..day6 import parse_data, part_one, part_two


def test_parse_data():
    assert parse_data("tests/data_test_day_6.txt") == [3, 4, 3, 1, 2]


data = parse_data("tests/data_test_day_6.txt")


def test_part_one():
    assert part_one(data, 80) == 5934


def test_part_two():
    assert part_two(data, 256) == 26984457539
