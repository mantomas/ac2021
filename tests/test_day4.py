from ..day4 import parse_data, play, win_last, winner_check, \
    calculate_score, board_check, main


drawn_numbers = [
    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,
    6,15,25,12,22,18,20,8,19,3,26,1
]
boards = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
]

def test_parse_data():
    assert parse_data("tests/data_test_day_4.txt") == (drawn_numbers, boards)
    

def test_calculate_score():
    assert calculate_score(
        [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
        [1,7,4,9,5,11,17,23,2,0,14,21,24]
    ) == 4512


def test_winner_check():
    assert winner_check(
        [7,4,9,5,11,17,23,2,0,14,21,24],
        boards
    ) == [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    assert winner_check(
        [7,4,9,5,11,17,23,2,0,14,21],
        boards
    ) == False
    assert winner_check(
        [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13],
        [[
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ]]
    ) == [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ]


def test_play():
    assert play(drawn_numbers, boards) == 4512


def test_win_last():
    assert win_last(drawn_numbers, boards) == 1924


def test_board_check():
    assert board_check(
        [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
        [7,4,9,5,11,17,23,2,0,14,21,24]
    )
    assert board_check(
        [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
        [7,4,9,5,11,17,23,2,0,14,21]
    ) == False


def test_main(capsys):
    main("tests/data_test_day_4.txt")
    captured = capsys.readouterr()
    assert "4512" in captured.out
    assert "1924" in captured.out
