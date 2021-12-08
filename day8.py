import re
from typing import List, Tuple, Dict


# PART 1
def parse_data_part_one(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        content: List[str] = f.readlines()
        group_of_four: List[str] = [line.split("|")[1].strip() for line in content]
        return group_of_four


def part_one(data: List[str]) -> int:
    count_unique: int = 0
    for pattern in data:
        for group in pattern.split():
            if len(group) in (2, 3, 4, 7):
                count_unique += 1
    return count_unique


# PART 2
def parse_data_part_two(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name, "r") as f:
        content: List[str] = f.readlines()
        line_tuples: List[Tuple[str, str]] = [
            (line.split("|")[0].strip(), line.split("|")[1].strip()) for line in content
        ]
        return line_tuples


def decode_positions(pattern: str) -> Dict[str, str]:
    # signals without pattern for 8
    signals: List[str] = sorted(pattern.split(), key=len)[:-1]
    fixed_letters: str = ""  # Helper string
    positions = {
        "T": ["", "a"],
        "M": ["", "d"],
        "B": ["", "g"],
        "LT": ["", "b"],
        "LB": ["", "e"],
        "RT": ["", "c"],
        "RB": ["", "f"],
    }
    # initial RT & RB and remove pattern
    positions["RT"][0] = positions["RB"][0] = signals.pop(0)
    # setting of T and remove pattern
    for i in signals.pop(0):
        if i not in positions["RT"][0]:
            positions["T"][0] = i
    fixed_letters += positions["T"][0]
    # initial M & LT and remove pattern
    for i in signals.pop(0):
        if i not in positions["RT"][0]:
            positions["M"][0] += i
            positions["LT"][0] += i
    # setting B & M from 3
    for i in signals[:3]:
        if all(letter in i for letter in positions["RT"][0]):
            subpattern = signals.pop(signals.index(i))
            # setting B
            for j in subpattern:
                if (
                    j not in positions["RT"][0]
                    and j not in positions["T"][0]
                    and j not in positions["M"][0]
                ):
                    positions["B"][0] = j
                    fixed_letters += positions["B"][0]

            # setting M
            for k in subpattern:
                if (
                    k not in positions["RT"][0]
                    and k not in positions["T"][0]
                    and k not in positions["B"][0]
                ):
                    positions["M"][0] = k
                    fixed_letters += positions["M"][0]
    # setting LB & RT from number 2
    for i in signals[:2]:
        if not all(
            (letter in i for letter in fixed_letters)
            and (letter in i for letter in positions["RB"][0])
            and (letter in i for letter in positions["LT"][0])
        ):
            subpattern = signals.pop(signals.index(i))
            for j in subpattern:
                if j not in positions["RT"][0] and j not in fixed_letters:
                    positions["LB"][0] = j
                    fixed_letters += positions["LB"][0]
            for k in subpattern:
                if k not in fixed_letters:
                    positions["RT"][0] = k
                    fixed_letters += positions["RT"][0]
    # setting RB from RT
    for i in positions["RB"][0]:
        if i not in positions["RT"][0]:
            positions["RB"][0] = i
            fixed_letters += positions["RB"][0]
    # setting LT from fixed_positions
    for i in positions["LT"][0]:
        if i not in fixed_letters:
            positions["LT"][0] = i
    return {x[0]: x[1] for x in positions.values()}


def calculate_number(subpattern: List[str], positions: Dict[str, str]):
    str_numbers = ""
    numbers_compositions = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }
    for word in subpattern:
        converted = ""
        for letter in word:
            converted += positions[letter]
        str_numbers += numbers_compositions["".join(sorted(converted))]
    return int(str_numbers)


def part_two(data: List[Tuple[str, str]]) -> int:
    decoded_numbers: List[int] = []
    for line in data:
        positions = decode_positions(line[0])
        number = calculate_number(line[1].split(), positions)
        decoded_numbers.append(number)
    return sum(decoded_numbers)


def main(file_name: str) -> Tuple[int, int]:
    data_part_one: List[str] = parse_data_part_one(file_name)
    data_part_two = parse_data_part_two(file_name)
    count_part_one = part_one(data_part_one)
    count_part_two = part_two(data_part_two)
    return count_part_one, count_part_two


if __name__ == "__main__":
    part_1, part_2 = main("day_8_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
