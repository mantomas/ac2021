from ..day7 import parse_data, part_one, part_two, cost_part_one, cost_part_two


def test_parse_data():
    assert parse_data("tests/data_test_day_7.txt") == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_cost_part_one():
    assert cost_part_one(2, [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]) == 37


def test_part_one():
    data = parse_data("tests/data_test_day_7.txt")
    assert part_one(data) == 37


def test_cost_part_two():
    assert cost_part_two(5, [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]) == 168


def test_part_two():
    data = parse_data("tests/data_test_day_7.txt")
    assert part_two(data) == 168
