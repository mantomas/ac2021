from ..day13 import parse_data, part_one, part_two


def test_parse_data():
    data = parse_data("tests/data_test_day_13.txt")
    assert data[0] == [
        (6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11),
        (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4),
        (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0)
        ]
    assert data[1] == [
        ("y", 7), ("x", 5)
    ]


def test_part_one():
    assert part_one("tests/data_test_day_13.txt") == 17


def test_part_two(capsys):
    part_two("tests/data_test_day_13.txt")
    captured = capsys.readouterr()
    assert "#####" in captured.out
    assert "#   #" in captured.out
