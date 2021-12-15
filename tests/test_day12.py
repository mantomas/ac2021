from ..day12 import parse_data, part_one, part_two


def test_parse_data():
    example_one = parse_data("tests/data_test_day_12.txt")
    example_two = parse_data("tests/data_test_day_12B.txt")
    assert example_one['start'] == ['HN', 'kj', 'dc']
    assert example_one['end'] == ['dc', 'HN']
    assert example_two['start'] == ['DX', 'pj', 'RW']
    assert example_two['end'] == ['fs', 'zg']


def test_part_one():
    assert part_one("tests/data_test_day_12.txt") == 19
    assert part_one("tests/data_test_day_12B.txt") == 226


def test_part_two():
    assert part_two("tests/data_test_day_12.txt") == 103
    assert part_two("tests/data_test_day_12B.txt") == 3509
