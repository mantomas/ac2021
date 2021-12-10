from ..day9 import mark_neighbours, parse_data_part_one, part_one, part_two, \
    get_coordinates, calculate_size, get_field


def test_parse_data_part_one():
    assert parse_data_part_one("tests/data_test_day_9.txt") == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_part_one():
    assert part_one("tests/data_test_day_9.txt") == 15


def test_get_coordinates():
    data = parse_data_part_one("tests/data_test_day_9.txt")
    assert get_coordinates(data) == [
        (0, 1, 1),
        (0, 9, 0),
        (2, 2, 5),
        (4, 6, 5),
    ]


def test_get_field():
    data = parse_data_part_one("tests/data_test_day_9.txt")
    assert get_field((2, 2, 5), data) == (
        [
            [2, 1, 9, 9, 9, 4],
            [3, 9, 8, 7, 8, 9],
            [9, 8, 5, 6, 7, 8],
            [8, 7, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6], 
        ],
        [
            [9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
            [9, 9, 5, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
        ]
    )
    assert get_field((0, 1, 1), data) == (
        [
            [2, 1, 9, 9, 9, 4, 3, 2, 1],
            [3, 9, 8, 7, 8, 9, 4, 9, 2],
            [9, 8, 5, 6, 7, 8, 9, 8, 9],
            [8, 7, 6, 7, 8, 9, 6, 7, 8],
            [9, 8, 9, 9, 9, 6, 5, 6, 7],
        ],
        [
            [9, 1, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9],
        ]
    )


def test_mark_neighbour():
    assert mark_neighbours(
        [
            [2, 1, 9, 9, 9, 4],
            [3, 9, 8, 7, 8, 9],
            [9, 8, 5, 6, 7, 8],
            [8, 7, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6], 
        ],
        [
            [9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
            [9, 9, 5, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9],
        ]
    ) == [
        [9, 9, 9, 9, 9, 9],
        [9, 9, 8, 7, 8, 9],
        [9, 8, 5, 6, 7, 8],
        [8, 7, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 9]
    ]


def test_calculate_size():
    data = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    assert calculate_size((2, 2, 5), data) == 14


def test_part_two():
    assert part_two("tests/data_test_day_9.txt") == 1134
