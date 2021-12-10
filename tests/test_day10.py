from ..day10 import corrupted_points, parse_data, part_one, \
    score, points, part_two


def test_parse_data():
    assert parse_data("tests/data_test_day_10.txt") == [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_corrupted_points():
    assert corrupted_points("{([(<{}[<>[]}>{[]{[(<()>") == 1197
    assert corrupted_points("[({(<(())[]>[[{[]{<()<>>") == 0
    assert corrupted_points("[<(<(<(<{}))><([]([]()") == 3


def test_part_one():
    assert part_one("tests/data_test_day_10.txt") == 26397


def test_score():
    assert score(['[', '(', '{', '(', '[', '[', '{', '{']) == 288957


def test_points():
    assert points("[({(<(())[]>[[{[]{<()<>>") == 288957


def test_part_two():
    assert part_two("tests/data_test_day_10.txt") == 288957
