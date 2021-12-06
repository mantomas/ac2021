from ..day5 import count_over_two, part_2_defaultdict, part_2_with_map, \
    parse_data, make_map_hv

def test_count_over_two_simple():
    data = parse_data("tests/data_test_day_5.txt")
    map_simple = make_map_hv(data)
    assert count_over_two(map_simple) == 5


def test_part_2_with_map():
    assert part_2_with_map("tests/data_test_day_5.txt") == 12


def test_part_2_defaultdict():
    assert part_2_defaultdict("tests/data_test_day_5.txt") == 12
