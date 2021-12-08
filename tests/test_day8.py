from ..day8 import parse_data_part_one, part_one, \
    parse_data_part_two, part_two, decode_positions, calculate_number


def test_parse_data_part_one():
    assert parse_data_part_one("tests/data_test_day_8.txt") == [
        "fdgacbe cefdb cefbgd gcbe",
        "fcgedb cgb dgebacf gc",
        "cg cg fdcagb cbg",
        "efabcd cedba gadfec cb",
        "gecf egdcabf bgf bfgea",
        "gebdcfa ecba ca fadegcb",
        "cefg dcbef fcge gbcadfe",
        "ed bcgafe cdgba cbgef",
        "gbdfcae bgc cg cgb",
        "fgae cfgab fg bagce",
    ]


def test_part_one():
    assert (
        part_one(
            [
                "fdgacbe cefdb cefbgd gcbe",
                "fcgedb cgb dgebacf gc",
                "cg cg fdcagb cbg",
                "efabcd cedba gadfec cb",
                "gecf egdcabf bgf bfgea",
                "gebdcfa ecba ca fadegcb",
                "cefg dcbef fcge gbcadfe",
                "ed bcgafe cdgba cbgef",
                "gbdfcae bgc cg cgb",
                "fgae cfgab fg bagce",
            ]
        )
        == 26
    )


def test_parse_data_part_two():
    assert parse_data_part_two("tests/data_test_day_8.txt") == [
        (
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb",
            "fdgacbe cefdb cefbgd gcbe",
        ),
        (
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec",
            "fcgedb cgb dgebacf gc",
        ),
        (
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef",
            "cg cg fdcagb cbg",
        ),
        (
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega",
            "efabcd cedba gadfec cb",
        ),
        (
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga",
            "gecf egdcabf bgf bfgea",
        ),
        (
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf",
            "gebdcfa ecba ca fadegcb",
        ),
        (
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf",
            "cefg dcbef fcge gbcadfe",
        ),
        (
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd",
            "ed bcgafe cdgba cbgef",
        ),
        (
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg",
            "gbdfcae bgc cg cgb",
        ),
        (
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc",
            "fgae cfgab fg bagce",
        ),
    ]



def test_decode_positions():
    assert decode_positions(
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
    ) == {'d': 'a', 'f': 'd', 'c': 'g', 'e': 'b', 'g': 'e', 'a': 'c', 'b': 'f'}


def test_calculate_number():
    subpattern = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
    positions = {'d': 'a', 'f': 'd', 'c': 'g', 'e': 'b', 'g': 'e', 'a': 'c', 'b': 'f'}
    assert calculate_number(subpattern, positions) == 5353



def test_part_two():
    data = parse_data_part_two("tests/data_test_day_8.txt")
    assert part_two(data) == 61229
